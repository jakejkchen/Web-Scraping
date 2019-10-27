import scrapy 
from phonelist.items import PhonelistItem
import re

class PhonelistSpider(scrapy.Spider):
	name = 'phonelist'
	allowed_urls = ['https://www.bestbuy.com']
	start_urls = ['https://www.bestbuy.com/site/searchpage.jsp?cp=2&searchType=search&_dyncharset=UTF-8&ks=960&sc=Global&list=y&usc=All%20Categories&type=page&id=pcat17071&iht=n&seeAll=&browsedCategory=pcmcat209400050001&st=categoryid%24pcmcat209400050001&qp=&sp=-bestsellingsort%20skuidsaas']
	
	#begin_url = 'https://www.bestbuy.com/site/reviews/'
	def parse(self, response):
		start_list_num = re.search(r'(.*)-(.*) of',response.xpath('//*[@id="resultsTabPanel"]/div[4]/div/div[1]/div/text()').extract()[0]).group(1)
		end_list_num =  re.search(r'(.*)-(.*) of',response.xpath('//*[@id="resultsTabPanel"]/div[4]/div/div[1]/div/text()').extract()[0]).group(2)
		num_list = int(end_list_num) - int(start_list_num) + 1

		for i in range(num_list):
			carrier = response.xpath('//h4/a/text()').re(r'.*\((.*)\)')[i]
			phone = response.xpath('//h4/a/text()').re(r'(.*) \(.*\)')[i]
			model = response.xpath('//*[@class="model-number"]/span[2]/text()').extract()[i]
			begin_url = 'https://www.bestbuy.com/site/reviews/'
			end_url = response.xpath('//*[@id="resultsTabPanel"]//h4/a/@href').re(r'\/site\/(.*)\.p.*')[i]
			url = begin_url + end_url 

			item = PhonelistItem()
			item['carrier'] = carrier
			item['phone'] = phone
			item['model'] = model
			item['url'] = url

			yield item

		next_page = response.xpath('//*[@class="pager-next"]/a/@href').extract_first()
		yield scrapy.Request(next_page, callback = self.parse)


