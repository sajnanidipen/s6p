import requests
from bs4 import BeautifulSoup

URL="http://values.com"
r=requests.get(URL)

soup=BeautifulSoup(r.content,'html5lib')
print(soup.prettify())
