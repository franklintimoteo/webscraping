# -*- coding: utf-8 -*-

from time import strftime, tzset
import os
import re

import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

""" Muda time zone para o Brasil """
os.environ['TZ'] = 'America/Sao_Paulo'
tzset()

def plf_get():
    """Retorna uma lista de links
    Essa função busca a coluna de conteudo do site
    retornando os links das postagens atuais
    """
    linkList = set()
    url = 'http://portallinuxferramentas.blogspot.com.br'
    try:
        html = requests.get(url)
    except ConnectionError:
        return None

    try:
        bsobj = BeautifulSoup(html.content, 'html.parser')
        
        #### Testa se a data atual é igual a da publicação
        today = strftime('%d')
        postDay = bsobj.find('div', {'class':'date-posts'}).find('abbr')['title']
        if postDay is not None:
            postDay = re.search('^[0-9]+\-[0-9]+\-[0-9]+', 
                                postDay).group().split('-')[-1]
            if today != postDay:
                return None
        ##### Fim
        column = bsobj.find('div', {'class':'date-posts'}).find_all('div', 
                    {'class':'post-outer'})
        if column is not None:
            for row in column:
                linkList.add(row.find('h3').a['href'])
        return linkList
    except AttributeError:
        return None
print(plf_get())