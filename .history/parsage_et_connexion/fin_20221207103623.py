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
    return x=1

#recuperation des donnees de la page
requet=requests.get(url)
pag=requet.content
soup=BeautifulSoup(pag, "html.parser")
print(soup)
f1=open("page de connexion.html", "w", encoding="utf-8")
f1.write(str(soup))
f1.close()

