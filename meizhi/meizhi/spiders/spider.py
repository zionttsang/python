import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from meizhi.items import MeizhiItem

class Spider(scrapy.Spider):
	name = "meizhi"
	allow_domains = ["https://www.baidu.com/"]
	# start_url_head = "https://www.zhihu.com/collection/38624707?page="
	
	def start_requests_pages(self):
		# for i in range(1,1):
			# url = self.start_url_head + str(i)
			# yield Request(url,self.parse)
		yield Request("https://www.baidu.com/",self.parse)
	
	def parse(self,response):
		print(response.text)
		