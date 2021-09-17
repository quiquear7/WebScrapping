import requests
import re
from bs4 import BeautifulSoup

URL_WIKIE = "https://es.wikipedia.com/"

def getTitle(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup.title)


def getHTREFs(URL):
    # Use a breakpoint in the code line below to debug your script.
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')
    hrefs = soup.find_all('a', href=True)
    for a in hrefs:
        print(a['href'])

def getIMGS(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'lxml')
    hrefs = soup.find_all('img', src=re.compile(r'.logo.'))
    for a in hrefs:
        print(a)

if __name__ == '__main__':
    getTitle(URL_WIKIE)
    getHTREFs(URL_WIKIE)
    getIMGS(URL_WIKIE)
