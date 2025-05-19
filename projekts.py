import re
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from docx import Document



lapas_url = "https://edition.cnn.com/"

try:
    atbilde = requests.get(lapas_url, timeout= 100)
    atbilde.raise_for_status()
except Exception as e:
    print(f"kļūda iegūstot mājaslapas informāciju!")
    exit(1)
lapas_info = BeautifulSoup(atbilde.text, 'html.parser')
visas_saites = lapas_info.find_all('a', href= True)
rakstu_saites = []
redzetas_saites = set()
for saite in visas_saites:
    href = saite['href']
    teksts = saite.get_text(strip= True)
    
    if '/202' in href and teksts and href not in redzetie:
        redzetas_saites.add(href)
        if not href.startswith("http"):
            href = "https://edition.cnn.com/"
        rakstu_saites.append(teksts, href)
    if len(rakstu_saites) == 5:
        break