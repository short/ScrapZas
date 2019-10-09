import requests
import urllib
import bs4script
import scrapyscript
import deeplinkscraper


def main():
    # Google search op keywords om URLS te verzamelen

    # Get URLS from search list an loop
    deeplinkscraper.crawl("https://nu.nl")


if __name__ == "__main__":
    main()
