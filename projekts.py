import re
from datetime import datetime
import requests #<-- bibliotēka priekš html
from bs4 import BeautifulSoup #<-- datascraping bibliotēka
from docx import Document



lapas_url = "https://edition.cnn.com/"

try:
    atbilde = requests.get(lapas_url, timeout= 100)
    atbilde.raise_for_status()
except Exception as e:
    print(f"kļūda iegūstot mājaslapas informāciju!")
    exit(1)
lapas_info = BeautifulSoup(atbilde.text, 'html.parser') #<-- šeit tiek glabāta informācija
visas_saites = lapas_info.find_all('a', href= True)
rakstu_saites = [] #<-- saglabā visus ar 'href' piederību HTML tagus (Hypertext reference)
redzetas_saites = set() #<-- šeit saglabā visus 'href' tagus, kurus jau esam apskatījušies

for saite in visas_saites: 
    href = saite['href'] #<-- šeit izvelk URL no linka
    teksts = saite.get_text(strip= True) #<-- šeit izvelk nevajadzīgo informāciju no URL
    
    if '/2025' in href and teksts and href not in redzetie: #<-- šeit pārliecinamies, ka raksts ir par 2025.gadu, tajā nav tukšs teksts un šis ir neredzēts links
        redzetas_saites.add(href)
        if not href.startswith("http"):
            href = "https://edition.cnn.com/"
        rakstu_saites.append(teksts, href)
    if len(rakstu_saites) == 5:
        break

  doc = Document()
    sodien = datetime.now().strftime("%Y-%m-%d")
    docx_filename = f"{sidien}_cnn.docx"
       
    for idx, (virsraksts, saite) in enumerate(rakstu_saites, start=1):
        try:
            raksts = requuests.get(saite, timeout=10)
            raksts.raise_for_status()
        except Exception as e:
            print(f"klūda, iegūstot ziņu: {virsraksts} - {e}")
            continue
        raksts_soup = BeautifulSoup(raksts.text, 'html.parser')
        try virsraksts_teksts = raksts_soup.find('h1').get_text(strip=True)
        except Exception:
        virsrakstrs_teksts = virsraksts


   datums_teksts = "(nav atrasts)"
try:
    meta_tag = raksts_soup.find("meta",{"itemprop":"datepulished"}) or \
      raksts_soup.find("meta",{"name":"pubdate"}
    if meta_tag and meta_tag.get("content")::
        datums_teksts = meta_tag["content"].split("T")[0]
except Exception:
    pass
ievads_teksts= ""
if len(ievads_teksts)>150:
    saisinajums = ievads_teksts[:ievads_teksts.rfind('',0,150)]
    ievads_teksts = saisinajums + "..."
doc.add_paragraph(f"{idx}. Virsraksts{virsakts_taksts}")
doc.add_paragraph(f"Datums:{datums_teksts}")
doc.add_paragraph(f"Ievads:{ievads_teksts or 'Nav apraksta'}")
doc.add_paragraph(f" Saite:{saite}")
doc.add_paragraph("")

           



















