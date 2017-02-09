import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.http import Request
from meizhi.items import MeizhiItem
import random

import meizhi.zhihuLogIn
from meizhi.zhihuLogIn import isLogin,login,get_session

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
	start_url_head = 'http://www.zhihu.com/#signin'
		
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

		
	def after_login(self,response):
		print ('get in the after_signin')
		
		sel = Selector(response)
		for link in sel.xpath("//body//div//link/@href").extract():
			link_full = "https://www.zhihu.com" + link
			print ("link_full: ",link_full)
			
			yield Request(link_full, headers = self.headers, callback = self.parse_answer)
		
	def parse_answer(self,response):
		print("get in the parse_answer")
		
		sel = Selector(response)
		item = MeizhiItem()
		l = ItemLoader(item = MeizhiItem(), response = response)
		l.add_xpath('image_urls',"//body//div//main//div//span/img/@data-original",Identity()
		
		return l.load_item()
		
		# print ("text_test: ",sel.xpath('/body//div/main//div/span/img'))
		
		# for pic_url in sel.xpath("//body//div//main//div//span/img"):
		
			# test_image = pic_url.xpath("./@data-original").extract()[0]
			# print ("item: ",pic_url.xpath("./@data-original").extract()[0])
			
			# item['image_urls'] = [pic_url.xpath("./@data-original").extract()[0]]
			# yield item
	
	def get_xsrf(self):
		'''_xsrf 是一个动态变化的参数'''
		index_url = 'https://www.zhihu.com'
		# 获取登录时需要用到的_xsrf
		index_page = session.get(index_url, headers=headers)
		html = index_page.text
		pattern = r'name="_xsrf" value="(.*?)"'
		# 这里的_xsrf 返回的是一个list
		_xsrf = re.findall(pattern, html)
		return _xsrf[0]


	# 获取验证码
	def get_captcha(self):
		t = str(int(time.time() * 1000))
		captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
		r = session.get(captcha_url, headers=headers)
		with open('captcha.jpg', 'wb') as f:
			f.write(r.content)
			f.close()
		# 用pillow 的 Image 显示验证码
		# 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
		try:
			im = Image.open('captcha.jpg')
			im.show()
			im.close()
		except:
			print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
		captcha = input("please input the captcha\n>")
		return captcha