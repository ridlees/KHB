import requests
from bs4 import BeautifulSoup

def Get_text(url):
    return requests.get(url)

def Soup(page):
    return BeautifulSoup(page.content, 'html.parser')

def Get_links(url):
    soup = Soup(Get_text(url))
    meta = soup.findAll("mets:mets")[0]
    label = meta.get("label")
    links = meta.findAll('mets:file',{"mimetype":"text/plain"})
    urls = []
    for link in links:
        flocat = link.findAll("mets:flocat")[0]
        urls.append(flocat.get("xlink:href"))
    return urls,label

def Crawl(url):
    urls, label = Get_links(url)
    with open(f'{label}.txt' ,"w+") as save:
        for link in urls:
            text = Soup(Get_text(link)).text
            save.write(text)




#Crawl("http://kramerius.nkp.cz/kramerius/mets/ABA001/819462")
#Crawl("http://kramerius.nkp.cz/kramerius/mets/ABA001/12055235")
Crawl("http://kramerius.nkp.cz/kramerius/mets/ABA001/11797323")
