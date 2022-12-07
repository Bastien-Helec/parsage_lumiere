from authentif_lib import   * 

def find_login_form(html_form):
    return html_form.attrs['action'].startswith('login.php')

br = mechanize.Browser()
br.open('http://developpez.net/forums/')
br.select_form(predicate=find_login_form)
br.form.set_value('bastien.helec@etu.umontpellier.fr', name='vb_login_username')
br.form.set_value('MOTDEPASSE', name='vb_login_password')
br.submit()
br.follow_link(url='http://developpez.net/forums/')
br.follow_link(url_regex=r'private.php$')
print(br.title())
br.close()