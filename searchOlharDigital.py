from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

"""Esse webcrawler obtem os titúlos/url/imagens das útlimas
publicações do Olhar Digital.
Desenvolvido para funcionar em .../noticias
Retorna um dicinário {Title:url}
Limite 03"""
def getTitle(url, limit=3):
    titleList = {}
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        objBs = BeautifulSoup(html, "html.parser")
        content = objBs.find_all("div", {"class":"main-item"},limit=limit)
        if content is not None:
            for title in content:
                titleList[title.h3.get_text()] = title.h3.find("a")["href"]
        return titleList
    except AttributeError:
        return None

"""Retorna o url das imagens. Limite 03"""
def getImg(url, limit=3):
    imageList = set()
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        objBs = BeautifulSoup(html, "html.parser")
        content = objBs.find_all("div", {"class":"post-img"}, limit=limit)
        if content is not None:
            for img in content:
                imageList.add(img.find("img")["src"])
        return imageList
    except AttributeError:
        return None

