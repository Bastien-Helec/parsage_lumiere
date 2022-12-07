# modules 
from authentif_lib import * 

# authentification visuelle
url = ""
login = "Mrnunus"
password = ""

# la requete et reponse de la page

browser = mechanize.Browser()
browser.open(url)
browser.select_form(nr = 0)
browser.form['username'] = login
browser.form['password'] = password
browser.submit()
browser.response().read()
