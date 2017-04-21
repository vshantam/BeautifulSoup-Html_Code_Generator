import sys
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
url=#Post your url "
try:
  get_url=urlopen(url)
  get_code=get_url.read()
  soup=BeautifulSoup(get_code,'lxml')
  print(soup.find_all('html')[0])
except HTTPError:
  print("Server error\nTry again later\n")
except Excetion as e:
  print(str(e))
