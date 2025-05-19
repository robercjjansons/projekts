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




















