
"""
pii_scanner.py

Scans a PDF file (local) and extracts possible PII:
- PERSON (spaCy NER -> names / surnames)
- email, phone, codice fiscale (IT), IBAN, credit card-like sequences
Outputs JSON report and can produce a redacted text/HTML file.

Usage:
    python pii_scanner.py input.pdf --redact --out report.json

Notes:
- Works best on machine-generated PDFs. For scanned PDFs, OCR (tesseract) is needed first.
- Processing is local; no network calls performed by this script.

"""

import re
import json
import argparse
from pathlib import Path
from collections import defaultdict
import pdfplumber

# Optional imports
try:
    import spacy
    NLP = spacy.load("it_core_news_sm")
except Exception as e:
    NLP = None
    # we'll handle in code: if None, skip NER and warn.

# optional stdnum for IBAN validation
try:
    from stdnum import iban as std_iban
except Exception:
    std_iban = None

# ---------- Patterns ----------
EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
# Simple italian phone detection: allows +39, 0039, ( +39 ) or none, and 6-12 digits possibly separated by spaces/dots/hyphens
PHONE_RE = re.compile(r"(?:\+39|0039|\(\\+39\)|\(?\+39\)?\s?)?\s*(?:\d[\s\.\-]?){6,12}\d")
# Codice fiscale (basic format): 16 alnum, pattern commonly used
CODICE_FISCALE_RE = re.compile(r"\b[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]\b", re.IGNORECASE)
# Simpler alternative if lowercase or variants allowed
CODICE_FISCALE_SIMPLE = re.compile(r"\b[A-Za-z]{6}[0-9]{2}[A-Za-z][0-9]{2}[A-Za-z][0-9]{3}[A-Za-z]\b")

# IBAN (simple): starts with 2 letters country code + 2 digits + up to 30 alnum
IBAN_RE = re.compile(r"\b[A-Z]{2}[0-9]{2}[A-Z0-9]{10,30}\b", re.IGNORECASE)

# Credit card like: 13-19 digits groups possibly separated
CC_RE = re.compile(r"\b(?:\d[ -]*?){13,19}\b")

# Generic name-like heuristics: fallback regex for "Nome: <word>" or "Cognome: <word>"
NAME_FIELD_RE = re.compile(r"\b(?:nome|cognome|nominativo|ragione sociale)\s*[:\-]\s*([A-Z][a-zàèéìòù'\-]{1,40})", re.IGNORECASE)

# ---------- Helper functions ----------
def extract_text_from_pdf(path: Path) -> str:
    text_parts = []
    with pdfplumber.open(str(path)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_parts.append(text)
    return "\n\n".join(text_parts)

def find_regex_all(pattern, text):
    return [{"match": m.group(0), "span": m.span()} for m in pattern.finditer(text)]

def maybe_validate_codice_fiscale(cf: str) -> dict:
    """
    Basic format check + placeholder for full validation.
    For production: implement the full checksum + omocodia handling if needed.
    """
    cf = cf.strip().upper()
    result = {"value": cf, "format_ok": False, "checksum_ok": None, "notes": []}
    if CODICE_FISCALE_SIMPLE.fullmatch(cf):
        result["format_ok"] = True
    else:
        result["notes"].append("Formato non standard")
    # checksum algorithm not implemented here; user can extend.
    result["checksum_ok"] = None
    result["notes"].append("Controllo checksum non eseguito (opzionale da implementare)")
    return result

def simple_luhn_check(number_str: str) -> bool:
    # Remove non digits
    s = re.sub(r"\D", "", number_str)
    total = 0
    reverse_digits = s[::-1]
    for i, ch in enumerate(reverse_digits):
        d = int(ch)
        if i % 2 == 1:
            d = d * 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def detect_names_spacy(text: str):
    if NLP is None:
        return []
    doc = NLP(text)
    persons = []
    for ent in doc.ents:
        if ent.label_ == "PER" or ent.label_ == "PERSON":
            persons.append({"text": ent.text, "span": (ent.start_char, ent.end_char)})
    return persons

def mask_text(text: str, spans: list, mask="█"):
    """
    Given text and list of spans (start,end) masks those spans.
    Spans must be non-overlapping or we'll handle by sorting.
    """
    if not spans:
        return text
    spans_sorted = sorted(spans, key=lambda s: s[0])
    out = []
    last = 0
    for s,e in spans_sorted:
        out.append(text[last:s])
        out.append(mask * max(4, e - s))  # at least 4 blocks so masked part isn't trivially reversible
        last = e
    out.append(text[last:])
    return "".join(out)

# ---------- Main scanning ----------
def scan_text_for_pii(text: str) -> dict:
    findings = defaultdict(list)

    # emails
    for m in EMAIL_RE.finditer(text):
        findings["emails"].append({"value": m.group(0), "span": m.span()})

    # phones
    for m in PHONE_RE.finditer(text):
        # naive filter: phone should have >=6 digits
        digits = re.sub(r"\D", "", m.group(0))
        if len(digits) >= 6:
            findings["phones"].append({"value": m.group(0).strip(), "span": m.span()})

    # codice fiscale (aggressive)
    for m in CODICE_FISCALE_SIMPLE.finditer(text):
        cf = m.group(0)
        findings["codice_fiscale"].append(maybe_validate_codice_fiscale(cf) | {"span": m.span()})

    # IBAN
    for m in IBAN_RE.finditer(text):
        candidate = m.group(0).replace(" ", "")
        valid = None
        if std_iban:
            try:
                valid = std_iban.is_valid(candidate)
            except Exception:
                valid = None
        findings["ibans"].append({"value": candidate, "span": m.span(), "valid": valid})

    # credit-card-like
    for m in CC_RE.finditer(text):
        s = re.sub(r"\D", "", m.group(0))
        # heuristic: credit card numbers typically length 13-19 and pass Luhn
        if 13 <= len(s) <= 19:
            luhn = simple_luhn_check(s)
            findings["credit_card_candidates"].append({"value": m.group(0), "span": m.span(), "luhn_ok": luhn})

    # name fields (heuristic)
    for m in NAME_FIELD_RE.finditer(text):
        findings["name_fields"].append({"value": m.group(1), "span": m.span()})

    # spaCy NER for PERSON
    persons = detect_names_spacy(text)
    for p in persons:
        findings["persons_ner"].append(p)

    return findings

# ---------- CLI and output ----------
def main():
    parser = argparse.ArgumentParser(description="PII scanner for PDFs (local).")
    parser.add_argument("pdf", type=str, help="Path to PDF file")
    parser.add_argument("--out", type=str, default="pii_report.json", help="Output JSON report file")
    parser.add_argument("--redact", action="store_true", help="Create a redacted text file next to the PDF")
    parser.add_argument("--redact-html", action="store_true", help="Create a simple redacted HTML with highlights")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"[ERROR] File non trovato: {pdf_path}")
        return

    print("[*] Estrazione testo dal PDF...")
    text = extract_text_from_pdf(pdf_path)
    if not text.strip():
        print("[WARN] Nessun testo estratto. PDF potrebbe essere scannerizzato (OCR necessario).")
    print("[*] Scansione PII...")
    findings = scan_text_for_pii(text)

    # Prepare simplified report (remove spans for readability in JSON unless needed)
    report = {
        "file": str(pdf_path),
        "summary": {k: len(v) for k, v in findings.items()},
        "details": findings
    }

    # Save report
    out_path = Path(args.out)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"[*] Report salvato: {out_path}")

    # Redaction (text) if requested: mask all spans we found
    if args.redact or args.redact_html:
        # collect spans
        spans = []
        for k, items in findings.items():
            for it in items:
                sp = it.get("span")
                if sp and isinstance(sp, (list, tuple)) and len(sp) == 2:
                    spans.append(tuple(sp))
        if spans:
            redacted = mask_text(text, spans)
            if args.redact:
                rpath = pdf_path.with_suffix(".redacted.txt")
                rpath.write_text(redacted, encoding="utf-8")
                print(f"[*] Redacted text salvato: {rpath}")
            if args.redact_html:
                # simple HTML with matches highlighted (non-robust; spans refer to text positions)
                html = "<html><body><pre style='white-space:pre-wrap;font-family:monospace'>"
                html += redacted.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
                html += "</pre></body></html>"
                hpath = pdf_path.with_suffix(".redacted.html")
                hpath.write_text(html, encoding="utf-8")
                print(f"[*] Redacted HTML salvato: {hpath}")
        else:
            print("[*] Nessuna occorrenza con span per redazione.")

if __name__ == "__main__":
    main()
