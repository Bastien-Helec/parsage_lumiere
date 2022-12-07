from authentif_lib import * 


url = "https://www.french-stream.al/accounts/login/"
login = "Mrnunus"
password = "Laforethb34"

a=''
request= urllib3.PoolManager()
# response = request.request("GET", url)
# forms = mechanize.make_response(response, headers=a)

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
    print("c'est bon :)")
except (urllib3.HTTPError, response3):
    print ("c'est pas bon :( ")