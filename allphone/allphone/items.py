# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AllphoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    carrier = scrapy.Field()
    phone = scrapy.Field()
    model = scrapy.Field()
    ave_rating = scrapy.Field()
    percent_recommend = scrapy.Field()
    rating = scrapy.Field()
    date = scrapy.Field()
    recommend = scrapy.Field()
