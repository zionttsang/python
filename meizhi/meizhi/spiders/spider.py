import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.http import Request
from meizhi.items import MeizhiItem
import random

from scrapy.contrib.loader import ItemLoader, Identity
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# import meizhi.zhihuLogIn
# from meizhi.zhihuLogIn import isLogin,login,get_session

class Spider(scrapy.Spider):
	
	# 构造 Request headers
	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, sdch, br',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Connection':'keep-alive',
		'Cache-Control':'max-age=0'
		,'Host':'www.zhihu.com'
		,'Upgrade-Insecure-Requests':'1'
		,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
	}

	name = "meizhi"
	allow_domains = ["https://www.zhihu.com/"]
	# start_url_head = 'http://www.zhihu.com/#signin'
		
	def start_requests(self):
		# account = input("account: ")
		# secret = input("password: ")
		# if meizhi.zhihuLogIn.isLogin():
			# print ("you have loged in")
		# else:
			# print("you need log in now")
			# meizhi.zhihuLogIn.login(secret,account)
		
		# global session
		# session = meizhi.zhihuLogIn.get_session()
		# print("now we print session")
		# print(session)
		# print("now we finished pirnt session")
		
		yield Request("https://www.zhihu.com/collection/38624707?page=1",headers = self.headers, callback = self.after_login)

	def __init__(self):
		# self.dcap = dict(DesiredCapabilities.PHANTOMJS)
		# self.dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0")
		
		self.driver = webdriver.PhantomJS(executable_path = "D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe") 
		
	def __del__(self):
		self.driver.close()
		
	def after_login(self,response):
		print ('get in the after_signin')
		
		# self.driver.get(response.url)
		# print("log:",response.text.encode("gbk","ignore"))
		# exit(0)
		
		# item = MeizhiItem()
		
		sel = Selector(response)
		
		for link in sel.xpath("//body//div//link/@href").extract():
			link_full = "https://www.zhihu.com" + link
			print ("link_full: ",link_full)
			
			yield Request(link_full, headers = self.headers, callback = self.parse_answer)
		
	def parse_answer(self,response):
		print("get in the parse_answer")
		# print ("res text: ",response.text.encode("gbk","ignore"))
		
		# html = response.text
		# soup = BeautifulSoup(html)
		
		sel = Selector(response)
		item = MeizhiItem()
		
		# start browser
		self.driver.get(response.url)
		
		print ("log: ",response.text.encode("gbk","ignore"))
		# exit(0)
		
		# loading time interval
		time.sleep(2)
		
		# l = ItemLoader(item = MeizhiItem(), response = response)
		
		# print ("length of the images: ",len(soup.find_all("img")))
		# exit()
		# for tag_image in soup.find_all("img"):
			# link_image = tag_image.get("data-original")
			# if link_image != None:
				# print ("link_image: ",link_image)
				# item["image_urls"] = link_image
				# l.add_xpath("image_urls",link_image, Identity())
			# else:
				# continue
				
			# yield item
		
		for pic_url in sel.xpath("//body//div//main//div//span[@class = 'RichText CopyrightRichText-richText']"):		
			image_urls = pic_url.xpath("/@data-original").extract()[0]
			# l.add_xpath('image_urls', "//@data-original", Identity())
			print ("item: ",image_urls)			
			# item['image_urls'] = [pic_url.xpath("/@data-original").extract()[0]]
			yield item
			
			# return l.load_item()
