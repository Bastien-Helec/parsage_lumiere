from authentif_lib import * 


url = "https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login"
login = "bastien.helec@etu.umontpellier.fr"
password = "72iutJrs80po$i!?"

request= urllib3.PoolManager()
response = request.request("GET", url)
forms = mechanize.make_response(response, backwards_compat=False)

form = forms[0]
print("form:"), form

control = form.find_control("action", type="hidden")
print ("control.name, control.value, control.type:", control.name, control.value, control.type)
control.readonly = False
control.value = login
control.readonly = True
print ("control.name, control.value, control.type:", control.name, control.value, control.type)
control = form.find_control("password", type="password")
print ("control.name, control.value, control.type:", control.name, control.value, control.type)
control.value = password
print ("control.name, control.value, control.type:", control.name, control.value, control.type)

request2 = form.click() 
try:
    response3 = urllib3.urlopen(request2)
    print("c'est bon")
except (urllib3.HTTPError, response3):
    print ("c'est pas bon:")