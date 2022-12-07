from authentif_lib import   * 

def find_login_form(html_form):
    return html_form.attrs['action'].startswith('https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login')

br = mechanize.Browser()
br.open('https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login.php')
br.select_form(predicate=find_login_form)
br.form.set_value('bastien.helec@etu.umontpellier.fr', name='username')
br.form.set_value('72iutJrs80po$i!?', name='vb_login_password')
br.submit()
br.follow_link(url='https://cas.umontpellier.fr/cas/login?service=https://ent.umontpellier.fr/uPortal/Login.php')
br.follow_link(url_regex=r'private.php$')
print(br.title())
br.close()