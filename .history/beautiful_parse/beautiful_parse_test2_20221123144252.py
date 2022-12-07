from beautiful_parse import BeautifulSoup,requests*
# https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login
requet=requests.get("http://www.perdu.com")
pag=requet.content
soup=BeautifulSoup(pag, "html.parser")
print(soup)
f1=open("ah.html", "w", encoding="utf-8")
f1.write(str(soup))
f1.close()
