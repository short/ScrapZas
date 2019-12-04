from bs4 import BeautifulSoup
import requests
import time
import csv
from os import path
import codecs
import datetime
import hashlib


class WebScraper:

    url_list = []
    file_name = ''

    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def get_html(self, url):
        response = requests.get(url, timeout=50)                    #haalt info van website op
        content = BeautifulSoup(response.content, "html.parser")    #maakt er een beautifulsoup object van
        text = content.find_all(text=True)                          #Grijpt alle tekst van de html data
        output = ''
        blacklist = [                                               #blacklist voor het weglaten van html code
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script',
            'style',
            'href',
            #Er kunnen mogelijk meer elementen zijn die weggelaten kunnen worden
        ]

        for item in text:
            if item.parent.name not in blacklist:                       #controleert of het item niet in de blacklist
                output += u'{} '.format(item)                           #zit en voegt deze toe aan de output

        output = "".join([s for s in output.strip().splitlines(True) if s.strip()])     #stript alle open regels
        output = "".join(output.splitlines())                                           #alles op een lijn zetten
        output.replace("\n", " ")                                                       #alle \n weghalen
        output.replace(",", "")                                                         #alle komma's wegwerken
        print('ophalen van html')
        print(output)
        return output

    def read_file(self):
        file = open(self.file_name, "r")                            #opent bestand met opgegeven bestandsnaam
        for line in file:
            self.url_list.append(line)                              #leest elke URL uit en voegt deze toe aan een list
        file.close()

    @staticmethod
    def write_to_doc(self, content_file, url):
        file = 'websites.csv'
        time_scraped = datetime.datetime.now()
        md5_hash = hashlib.md5(content_file.encode('utf-8')).hexdigest()
        new_row = [url, content_file, time_scraped, md5_hash]
        print('weg schrijven van informatie')
        if path.exists(file):                                       #controleert of bestand al bestaat of niet
            with codecs.open(file, 'a', 'utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(new_row)                            #voegt nieuwe text van html pagina toe aan csv
                print('info toevoegen')
        else:
            with codecs.open(file, 'w', 'utf-8') as f:              #creëert nieuw bestand en maakt header row aan
                writer = csv.writer(f)                              #voegt hierbij ook nieuwe text van html pagina toe
                writer.writerow(['Website', 'Text', "Time scraped", "Hash"])
                writer.writerow(new_row)
                print('nieuw bestand aanmaken')

    def get_all_html(self):
        for url in self.url_list:                                   #elke URL uit de lijst zal worden doorlopen
            try:
                print(url)                                          #Hierbij wordt de inhoud van de URL opgevraagd via
                text = self.get_html(self, url)                     #de get_html functie
                self.write_to_doc(self, text, url)                  #De inhoud wordt samen met de URL weggeschreven
            except:
                time.sleep(5)                                       #een time sleep zodat er niet te snel opgevraagt wordt
                print('waiting...')
                continue
        print("klaar met invullen...")

    @staticmethod
    def run_scraper(self):
        scraper1.read_file()
        scraper1.get_all_html()


scraper1 = WebScraper('paginalijst-uniques.txt')    #aanmaken van scraper
scraper1.run_scraper(scraper1)      #laat de scraper de geselecteerde txt file URLs scrapen
