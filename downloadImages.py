import os
import requests

"""Criar diretorio caso não exista"""
dirImgs = "baixados"
if not os.path.exists(dirImgs):
    os.makedirs(dirImgs)

"""Baixar imagens com os nomes da url"""
def downloadImg(url):
    if(os.path.exists(dirImgs)):
        os.chdir(dirImgs)
    name = url.split('/')[-1]
    image = open(name,"wb")
    contentBinary = requests.get(url).content
    image.write(contentBinary)
    image.close()
    return
