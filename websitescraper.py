from bs4 import BeautifulSoup
import requests
import csv
import time

class webScraper:

    url_list = []
    file_name = ''

    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def get_html(self, url):
        response = requests.get(url, timeout=50)
        content = BeautifulSoup(response.content, "html.parser")
        return content

    def read_file(self):
        file = open("log - kopie.txt", "r")
        for line in file:
            self.url_list.append(line)
        file.close()

    def write_html_csv(self):
        for item in self.url_list:
            try:
                print(self.get_html(self,item))

            except:
                print("Even wachten...")
                time.sleep(5)
                continue




#read_file()
scraper1 = webScraper('log.txt')

#print(webScraper.get_html(scraper1,'http://www.nu.nl'))
#print(get_html(url))
scraper1.read_file()
scraper1.write_html_csv()