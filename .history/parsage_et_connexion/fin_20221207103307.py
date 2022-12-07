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
login = "bastien.helec@etu.umontpellier.fr"
password = "72iutJrs80po$i!?"

# la requete et reponse de la page

browser = mechanize.Browser()
browser.open(url)
browser.select_form(nr = 0)
browser.form['username'] = login
browser.form['password'] = password
browser.submit()
browser.response().read()

#recuperation des donnees de la page de connexion 
def find_login_form(html_form):
    return html_form.attrs['action'].startswith('https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login')

br = mechanize.Browser()
br.open('https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login.php')
br.select_form(predicate=find_login_form)
br.form.set_value('bastien.helec@etu.umontpellier.fr', name='username')
br.form.set_value('72iutJrs80po$i!?', name='password')
br.submit()
br.follow_link(url='')
br.follow_link(url_regex=r'private.php$')
print(br.title())
br.close()

