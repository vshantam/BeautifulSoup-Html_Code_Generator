import sys
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
url=#Post your url "
get_url=urlopen(url)
get_code=get_url.read()
soup=BeautifulSoup(get_code,'lxml')
print(soup.find_all('html')[0])
