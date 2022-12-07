import os 
import csv
import requests
from urllib.request import *
from bs4 import *
import mechanize
import urllib3

#connexion 
# authentification visuelle
url = "https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login"
urlparse=""

# la requete et reponse de la page
def connexion(login, password):
    browser = mechanize.Browser()
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['username'] = login
browser.form['password'] = password
browser.submit()
browser.response().read()

#recuperation des donnees de la page
requet=requests.get(url)
pag=requet.content
soup=BeautifulSoup(pag, "html.parser")
print(soup)
f1=open("page de connexion.html", "w", encoding="utf-8")
f1.write(str(soup))
f1.close()

