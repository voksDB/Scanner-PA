from bs4 import BeautifulSoup as bs
import requests as req
import urllib


base_url = "https://www.comune.lonatepozzolo.va.it/it"
page = req.get(url)

dom = bs(page.text, 'html')

print(dom.find_all('a'))






def trova_link_trasparenza(base_url):
    try:
        r = req.get(base_url, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"Errore nel caricamento di {base_url}: {e}")
        return None
    

