# -*- coding: utf-8 -*-
import scrapy


class SpideroneSpider(scrapy.Spider):
    name = 'spiderone'
    allowed_domains = ['www.nu.nl']
    start_urls = ['https://www.nu.nl/']

    custom_settings = {
        'FEED_URI': 'tmp/test.csv'
    }

    def parse(self, response):
        # Extracting the content using css selectors

        content = response.css('.column-content').extract()

        # Give the extracted content row wise
        for item in zip(content):
            # create a dictionary to store the scraped info
            scraped_info = {
                'content': item[0]
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
