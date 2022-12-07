# modules 
from authentif_lib import * 

# authentification visuelle
url = "https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login"
login = ""
password = ""

# la requete et reponse de la page

request= urllib3.PoolManager()
response = request.request("GET", url)
forms = mechanize.make_response(response)
