import re
from bs4 import BeautifulSoup
from searchOlharDigital import getImg
from searchVidaProgramador import getTirinha
from downloadImages import downloadImg


#url: http://olhardigital.uol.com.br/noticias
imageUrl = getImg("http://olhardigital.uol.com.br/noticias", limit=3)
if imageUrl is not None and (len(imageUrl)) > 0:
    for image in imageUrl:
        downloadImg(image)
        
imageUrl = getTirinha("http://vidadeprogramador.com.br/")
if imageUrl is not None and (len(imageUrl)) > 0:
    for image in imageUrl:
        downloadImg(image)

