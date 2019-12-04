import deeplinkscraper
from collections import Counter


def main():
    with open("scrape_urls.txt", 'r') as file:
        urllist = list()
        for link in file:
            urllist.append(link)

        for item in urllist:
            print("nieuwe zoekterm" + item)
            deeplinkscraper.crawl(item)


if __name__ == "__main__":
    main()
