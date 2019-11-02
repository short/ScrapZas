import requests
from bs4 import BeautifulSoup
import time
import re
import json

forumlink = "https://www.hotforum.nl/forum-overzicht/Business+en+Finance"
#geef hier je max bedrag op

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
#aanvraag = {'accept=true']
drugsgebruikers = []


def getuserlink():
    while True:
        a = requests.get(forumlink, headers=headers)
        b = a.content
        soup = BeautifulSoup(b, "html.parser")
        #print(soup)

        for li in soup.find_all(class_="Visit"):
            print(li.a.get('href'))

def getpageinfo(a):
    r = requests.post("https://www.hotforum.nl/forum/index.php?name=Scotty&amp;go=onderwerp&amp;id=910908&amp;subject=xtc-speed-ghb-wiet-247-leverbaar/&amp")
    scrape = requests.get(a, headers=headers)
    websitecontent = scrape.content
    soup = BeautifulSoup(websitecontent, "html.parser")
    print(soup)

    for li in soup.find_all(class_="onderwerp"):
        print()

def test():
    url = 'https://www.hotforum.nl/forum/index.php?name=Drugsinc&'
    payload = {
        "Host": "www.hotforum.nl",
        "Connection": "keep-alive",
        "Content-Length": 11,
        "Origin": "https://www.hotforum.nl",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "https://www.hotforum.nl/forum/Drugsinc",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
        "Cookie": "PHPSESSID=9he8o8mb1p32r302r9j1n5t8q7",
        "Upgrade-Insecure-Requests": 1,
        "accept": "true"
    }


    p = {"accept": "true"
    }


    # Adding empty header as parameters are being sent in payload
    requests.post('https://www.hotforum.nl/forum/index.php?name=Drugsinc&', data=p)
    print('werkt')
    getpageinfo('https://www.hotforum.nl/forum/Drugsinc')



test()

#getpageinfo('https://www.hotforum.nl/forum/Drugsinc')
#getuserlink()
