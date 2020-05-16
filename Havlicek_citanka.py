import requests
from bs4 import BeautifulSoup

def Get_text(url):
    return requests.get(url)

def Soup(page):
    return BeautifulSoup(page.content, 'html.parser')

def Paragraphs(para):
    text = ""
    for p in para:
        text = text + "\n" + p.text
    return text

def Ahrefs(url):
    soup = Soup(Get_text(url))
    ul = soup.findAll("ul")[-2]
    links = ul.findAll("a")

    urls = []
    for link in links:
        urls.append(f'https://cs.m.wikisource.org/{link.get("href","")}')
        
    return urls

def ScrapPage(url):
    soup = Soup(Get_text(url))
    para = soup.findAll('p')
    title = soup.findAll("td")[1].text.strip()

    text = Paragraphs(para)
    return text, title

def Save(text, title):
    with open(f'{title}.txt' ,"w+") as save:
        save.write(text)

def Scrap(url,isArticle=True):
    if isArticle:
        text, title = ScrapPage(url)
        Save(text, title)
        
    else:
        urls = Ahrefs(url)
        for url in urls:
            text, title = ScrapPage(url)
            Save(text, title)
'''


Scrap("https://cs.m.wikisource.org/wiki/%C4%8Cl%C3%A1nky_z_N%C3%A1rodn%C3%ADch_novin", False)

Scrap("https://cs.m.wikisource.org/wiki/%C4%8Cl%C3%A1nky_ze_Slovana", False)
'''
