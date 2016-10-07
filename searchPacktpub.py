import requests
from bs4 import BeautifulSoup

import os

"""Create a dir, case not exists"""
dirPDF = "PDFbaixados"
if not os.path.exists(dirPDF):
    os.makedirs(dirPDF)

def authentication(url):
    """Return a content from requests
    email:zefomi@cartelera.org
    pass:lovepackt
    """

    try:
        headers = {'User-agent':'Mozilla/5.0'}
        content = requests.post(url, auth=('zefomi@cartelera.org','lovepackt'),
                    headers=headers)
        return session.get(url)
    except HTTPError:
        return None

def download_book(url):
    """Download the book"""

    if(os.path.exists(dirPDF)):
        os.chdir(dirPDF)
    nameBook = url.split('/')[-2]+'.pdf'
    book = open(nameBook, 'wb')
    binaryContent = authentication(url).content
    book.write(binaryContent)
    book.close()
    return

def claim_book():
    """Main function
    Return True - Sucess
    or False - Unsucess
    """

    homeSite = "https://www.packtpub.com"
    url = 'https://www.packtpub.com/packt/offers/free-learning'
    html = authentication(url)
    if html is not None:
        try:
            bsObj = BeautifulSoup(html.content, 'html.parser')
            contentList = bsObj.find('div', {'class':'book-claim-token-inner'})
            claimLink = homeSite + contentList.parent['href']
            """One acess on link, for claim free book"""
            authentication(claimLink)
            
            numberPDF = claimLink.split('/')[-2]
            linkPDF = homeSite + '/ebook_download/'+numberPDF+'/pdf'
            download_book(linkPDF)
            return True
        except AttributeError:
            return None
    return False

print(claim_book())