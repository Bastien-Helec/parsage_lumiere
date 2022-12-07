# modules 
from authentif_lib import * 

# authentification visuelle
url = "https://www.french-stream.al/accounts/login/"
login = ""
password = ""

# la requete et reponse de la page

request= urllib3.PoolManager()
response = request.request("GET", url)
forms = mechanize.make_response(response)
