# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PhonelistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    carrier = scrapy.Field()
    phone = scrapy.Field()
    model = scrapy.Field()
    url = scrapy.Field()

