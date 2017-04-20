import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.http import Request
from meizhi.items import MeizhiItem
import random
import requests

from scrapy.contrib.loader import ItemLoader, Identity
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

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
		
	def start_requests(self):
		yield Request("https://www.zhihu.com/collection/38624707?page=1",headers = self.headers, callback = self.after_login)

	def __init__(self):
		# self.driver = webdriver.PhantomJS(executable_path = "D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe") 

		self.driver = webdriver.PhantomJS(executable_path = "/Volumes/apple hdd/phantomjs-2.1.1-macosx/bin/phantomjs")
		
	def __del__(self):
		self.driver.close()
		
	def after_login(self,response):
		print ('get in the after_signin')
		
		sel = Selector(response)
		
		for link in sel.xpath("//body//div//link/@href").extract():
			link_full = "https://www.zhihu.com" + link
			print ("link_full: ",link_full)
			
			yield Request(link_full, headers = self.headers, callback = self.parse_answer)
		
	def parse_answer(self,response):
		print("get in the parse_answer")
		
		html = response.text
		soup = BeautifulSoup(html)
		
		# sel = Selector(response)
		item = MeizhiItem()
		
		# self.driver.execute_script("window.scrollBy(0,10000)")
		# time.sleep(2)
		# self.driver.execute_script("window.scrollBy(0,20000)")
		# time.sleep(2)
		# self.driver.execute_script("window.scrollBy(0,30000)")
		# time.sleep(2)
		# self.driver.execute_script("window.scrollBy(0,40000)")
		# time.sleep(2)
	
		
		# loading time interval
		# time.sleep(2)

		lstImg = []#Create listImg Obj

		for linkImg in soup.find_all("img"):
			# print ("in circle")
			addressImg = linkImg.get("data-original")
			lstImg.append(addressImg)

		s = set(lstImg)

		for image_urls in s:		
			item['image_urls'] = [image_urls]
			yield item
