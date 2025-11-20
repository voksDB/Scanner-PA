### studio e analisi (pre game) (1/2 settimane)

#### norme e leggi
- studiare quali normative e obblighi le autorità pubbliche devono sostenere nella sezione amministrazione trasparente e in genere alla privacy del sito 
- identificare i _tipi di documenti


#### Studio del progetto TrasparenzAI

- esaminare documentazione trasparenzAI 
- come scarica i dati (crawler / scraper);
- che tipo di analisi effettua (estrazione testi, OCR, anonimizzazione);
- su quali dataset lavora (dataset PA, formati file);
- capire se è possibile copiare 

#### definizione delle debolezze cercate 

- Dati personali esposti nomi, firme, CF, indirizzi, telefoni.
- Dati sensibili o particolari: salute, appartenenze sindacali, ecc.
- Metadati pericolosi: informazioni nascoste in PDF (es. autore, username, path locali).
- Documenti non anonimizzati: CV, determine con allegati non depurati.
- Informazioni che possono favorire attacchi
	- email dirette del personale → phishing mirato;
    - nomi + ruoli → social engineering;
    - file Word/PDF con macro o link esterni;
    - directory listing aperti o URL prevedibili.


### definire l'architettura del sistema (1 settimana)

[Discovery siti PA] → [Crawling / download documenti PDF/HTML] →  [Parsing contenuti] → [Analisi privacy + sicurezza] → [Report automatico]

- _CRAWLER_: vedere se si può utilizzare quello di trasparenzAI 
-  _DOWNLOAD PDF/HTML_ anche qui, secondo me si può utilizzare... no... 
- _ANALYZER_ in 3 sotto-moduli: 
  1. privacy compliance (cookie banner, privacy policy GDPR)
  2. scanner sul testo (integrazione AI?)
  3. security scanner 
- report generator, vedere se anche qui può essere utile 


#### linguaggi e librerie usate? 

python... non credo ci sia troppo da discutere qui. 

___

### sviluppare i moduli (1 mese tutto )

#### 3.1 Crawler & dataset

- Parti dai siti già mappati da TrasparenzAI.
- Estrai e indicizza URL dei documenti PDF  HTML della sezione “Amministrazione Trasparente”.
- Salva un dataset locale con metadati (url, data, titolo, dimensione file).    

#### 3.2 Analisi documentale

- Estrai testo dai PDF (pdfminer.six, Apache Tika).
- Esegui OCR sui PDF scansionati.
- Rileva:
    - pattern di dati personali (regex + modelli NLP);
    - firme digitali scansionate;
    - indirizzi email e numeri di telefono;
    - CF o P.IVA;
    - nomi propri + ruoli.
- Analizza i metadati dei file (autore, software, timestamp).

#### 3.3 Analisi sicurezza

- Cerca possibili **vettori di attacco informativo**:
    - File accessibili da directory prevedibili;
    - URL con parametri sensibili (es. `?id=123`);
    - Link a documenti interni non anonimizzati;
    - Email pubblicate in chiaro (target per spear-phishing).

____ 

### assicurarsi che tutto funzioni e raccolta risultati (1 settimana)


### scrittura report e tesi (2 settimane minimo dai)



