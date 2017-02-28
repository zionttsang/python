
from tsang.items import TsangItem
from scrapy.selector import Selector
from scrapy.http import Request
import scrapy


class Spider(scrapy.Spider):
	name = "tsang"
	allow_domains = ["https://www.jianshu.com/"]




	def start_requests(self):
		yield Request("http://www.jianshu.com/p/36a39ea71bfd",callback = self.parse)

	def parse(self,response):
		sel = Selector(response)
		item = TsangItem()	
		for imgTag in sel.xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div/img"):
			item["image_urls"] = imgTag.xpath("./@data-original-src").extract()[0] #in a [ ]  # ./
			yield item