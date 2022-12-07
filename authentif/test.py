from authentif_lib import *

browser = mechanize.Browser()
browser.set_debug_http(True)
browser.set_debug_responses(True)
browser.set_debug_redirects(True)
response = browser.open("http://python.org/")