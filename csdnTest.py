

import urllib
import urllib.request
from bs4 import BeautifulSoup

data=urllib.request.urlopen("http://blog.csdn.net/itcastcpp/article/details/51095332").read()
soup=BeautifulSoup(data,"html5lib")#解析方式
print(soup.find("h1", "csdn_top").get_text())
print("-----------------")
print(soup.find("div", "markdown_views").p.get_text())
'''
datalist=soup.find_all("div","list_item article_item")
#print(datalist)
for line  in  datalist:
    print(line.find("span","link_title").a.get_text())
    print(line.find("span", "link_title").a.get("href"))
    print(line.find("div", "article_description").get_text())

'''
