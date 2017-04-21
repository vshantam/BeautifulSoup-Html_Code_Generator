import sys
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
url=#Post your url "
try:
  get_url=urlopen(url)#getting responses from the server.
  get_code=get_url.read()#Reads the Entire html code.
  soup=BeautifulSoup(get_code,'lxml')#parsing the web content.
  print(soup.find_all('html')[0])#Displays the entire html code and removes the unnecessary tabs, allingment,tags etc.
except HTTPError:
  print("Server error\nTry again later\n")
except Excetion as e:
  print(str(e))
