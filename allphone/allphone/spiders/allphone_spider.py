import scrapy
from allphone.items import AllphoneItem
import re
import pandas as pd

class IphonexSpider(scrapy.Spider):
	name = 'allphone'
	allowed_urls = ['https://www.bestbuy.com']
	
	phonelist = pd.read_csv("C:/Users/junkl/Documents/NYC Data Science Academy/Bootcamp/python_web_scraping/scrapy_project/allphone/phonelist.csv")
	start_urls = list(phonelist['url'])

	def parse(self, response):

		start_list_num = re.search(r'(.*)-(.*) of',response.xpath('//*[@id="footer-pagination"]/div/div[1]/div/span[2]/text()').extract()[0]).group(1)
		end_list_num =  re.search(r'(.*)-(.*) of',response.xpath('//*[@id="footer-pagination"]/div/div[1]/div/span[2]/text()').extract()[0]).group(2)
		num_list = int(end_list_num) - int(start_list_num) + 1

		for i in range(num_list):

		    carrier = response.xpath('//*[@class="product-title"]/a/text()').re(r'.*\((.*)\)')[0]
		    phone = response.xpath('//*[@class="product-title"]/a/text()').re(r'(.*) \(.*\)')[0]
		    model =  response.xpath('//*[@class="product-model-info"]/span[1]/text()').extract_first()
		    ave_rating = response.xpath('//*[@class="c-review-average"]/text()').extract_first()
		    percent_recommend = response.xpath('//*[@class="average-score percent"]/text()').extract_first()
		    rating = response.xpath('//div[5]//span[@class="c-review-average"]/text()').extract()[i]
		    date = response.xpath('//div[5]//div[@class="review-date"]/span/text()').extract()[i]
		    recommend = response.xpath('//div[5]//div[@class="recommended-item row"]/p/i').re(r'"ficon-(.*)"')[i]


		    item = AllphoneItem()
		    item['carrier'] = carrier
		    item['phone'] = phone
		    item['model'] = model
		    item['ave_rating'] = ave_rating
		    item['percent_recommend'] = percent_recommend
		    item['rating'] = rating
		    item['date'] = date
		    item['recommend'] = recommend

		    yield item


		next_page =  response.xpath('//*[@class="page next"]/a/@href').extract_first().replace('deviceClass=l', '')
		yield scrapy.Request(next_page, callback = self.parse)
