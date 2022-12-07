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
urlparse="https://proseconsult.umontpellier.fr/direct/?data=3903f2df9c018bfca669616974e1c21a4f51f7d91eb3648604d628113e82760dbed8d89011b8db3f565a6eba3fb421d313f6c63370d69630c73e5d47e7b4caa205b671755e2e313accf1c0ae7bea9fe2ffaaa69cbd14fea5a6d0111bfaa17a823cc1c3b4302fc5dd2762be0aa3a53986aa46015363b2752612a410752d15eaafd211eeb7936734e0cd7fd38213cedc0eec845302a004ead06829e11b88069c045ea08a24cebd3cdc97f49ddaad75861d7156a03c810656e952ac30aedcff6f6e,1"
login=input("username : ")
password=input("password : ")
x=0
# la requete et reponse de la page
def connexion():
    while x==0:
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
    f1=open("page de connexion.html", "w", encoding="utf-8")
    f1.write(str(soup))
    f1.close()

def parsage():
    while x==1:
        #recuperation des donnees de la page agenda
        requet=requests.get(urlparse)
        pag=requet.content
        soup=BeautifulSoup(pag, "html.parser")
        print(soup)
        f1=open("agenda.html", "w", encoding="utf-8")
        f1.write(str(soup))
        f1.close()

