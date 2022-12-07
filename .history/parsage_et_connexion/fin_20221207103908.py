import os 
import csv
import requests
from urllib.request import *
from bs4 import *
import mechanize
import urllib3
global x
#connexion 
# authentification visuelle
url = "https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login"
urlparse=""
login=input("username : ")
password=input("password : ")
x=0
# la requete et reponse de la page
def connexion():
    browser = mechanize.Browser()
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['username'] = login
    browser.form['password'] = password
    browser.submit()
    browser.response().read()
    x=1

#recuperation des donnees de la page
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

for script in soup(["script", "style"]):
    script.extract()  
text = soup.get_text()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)



while x>0:
    #recuperation des donnees de la page agenda

