from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import time


def getDate():
    objDate = time.localtime(time.time())
    formatedDate = "{:02d}/{:02d}/{}".format(objDate.tm_mday,
                                             objDate.tm_mon,
                                             objDate.tm_year)
    return formatedDate

"""Tipos de retorno: None: caso dia(postagem) for inferior ao atual
ou caso o conteudo não seja encontrado por algum erro."""
def getTirinha(url, limit=1):
    imageList = set()
    try:
        html = requests.get(url)
    except HTTPError:
        return None
    try:
        objBs = BeautifulSoup(html.content, "html.parser")
        content = objBs.find_all("div", {"class":"post"}, limit=limit)
        if content is not None:
            for img in content:
                if img.h1.small.get_text()[0:10] == getDate():
                    imageList.add(img.find("img")['src'])
        return imageList
    except AttributeError:
        return None
