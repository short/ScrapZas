import requests
from bs4 import BeautifulSoup
import re
import time
from os import path
import codecs
import csv
import re



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
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
        # "Cookie": "PHPSESSID=9he8o8mb1p32r302r9j1n5t8q7",
        "Upgrade-Insecure-Requests": 1,
        "accept": "true"
    }
# Adding empty header as parameters are being sent in payload
session = requests.Session()
test = session.post('https://www.hotforum.nl/forum/index.php?name=Drugsinc&', data=payload)

#deze functie werkt nu helemaal. Vraagt alle onderwerpen van het forum aan.
def getuserlink(link):
    for aantalkeer in range(71):#terug naar 71
        forumlink = link + ('/' + str(((aantalkeer)*20)))#moetnaar1


        a = requests.get(forumlink, headers=headers)
        b = a.content
        soup = BeautifulSoup(b, "html.parser")

        for li in soup.find_all(class_="Visit"):
            print(li.a.get('href'))
            zoekaantalonderwerpen(li.a.get('href'))


def zoekaantalonderwerpen(a):
    website = a
    lijst = []
    scrape = session.get(a, headers=headers)
    websitecontent = scrape.content
    soup = BeautifulSoup(websitecontent, "html.parser")

    for link in soup.findAll('a'):
        lijst.append(link.get('href'))
    listlen = len(lijst)
    print("lijstlengte is " + str(listlen))
    if listlen <= 6:
        nummer = listlen - 1
    elif lijst[6] != '':
        dezemoetwordengestript = lijst[6]
        nummer = re.sub("[^0-9]", "", dezemoetwordengestript)
        #print(website, nummer)
    else:
        nummer = 2
    getpageinfo(website, nummer)

def getpageinfo(a, nummer):
    print("type = " + str(type(nummer)) + " " + str(nummer))

    if isinstance(nummer, str):
        nummer = 2

    for aantal in range(int(nummer)):
        counter = 0
        websitelink = a + '/p'+ str(aantal + 1)
        scrape = session.get(websitelink, headers=headers)
        websitecontent = scrape.content
        soup = BeautifulSoup(websitecontent, "html.parser")

        for link in soup.find_all('a'):
            website = link.get('href')
            if website.startswith('https://www.hotforum.nl'):
                counter = counter+ 1
                if counter > 5:
                    print(website)
                    leeghalenvanforum(website)


def leeghalenvanforum(a):
    #hierzo zorgen we ervoor dat we ook de onderliggende pagina's pakken
    doorgaan = 1
    teller= 0
    while doorgaan == 1:
        #print("gaat goed")
        teller = teller + 1
        link = a + '/' + str(teller)
        #print(link)
        scrape = session.get(link, headers=headers)
        websitecontent = scrape.content
        soup = BeautifulSoup(websitecontent, "html.parser")
        #deze counter wordt gebruikt om alleen de 30 nuttige usernames + het bericht eraf te halen
        counter = 0
        table_body = soup.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            #time.sleep(1)
            test2 = row.find_all('b', {"class": "onderwerp2"})
            test3 = test2 + row.find_all('b')
            test = row.find_all('span', {"class": "border"})
            cols = test + row.find_all('span')
            extra = test3 + cols
            extra = [x.text.strip() for x in extra]
            counter = counter + 1
            if counter > 6 and counter < 36:
                write_to_doc(extra)
                #print(extra)
                #print(len(extra))
                if len(extra) == 2:
                    doorgaan = 0
                    #print(doorgaan)
            elif counter > 38:
                counter = 0
                if len(extra) == 2:
                    doorgaan = 0



def write_to_doc(bericht):
    file = 'hotforum.csv'
    #print('weg schrijven van informatie')
    if path.exists(file):  # controleert of bestand al bestaat of niet
        with codecs.open(file, 'a', 'utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(bericht)  # voegt nieuwe text van html pagina toe aan csv
            #print('info toevoegen')
    else:
        with codecs.open(file, 'w', 'utf-8') as f:  # creëert nieuw bestand en maakt header row aan
            writer = csv.writer(f)  # voegt hierbij ook nieuwe text van html pagina toe
            writer.writerow(['username', 'date posted', "message"])
            writer.writerow(bericht)
            #print('nieuw bestand aanmaken')




getuserlink("https://www.hotforum.nl/forum-overzicht/Business+en+Finance")
#leeghalenvanforum('https://www.hotforum.nl/forum/Drugsinc/836350/snuifcoke-bezorg-service-247/')