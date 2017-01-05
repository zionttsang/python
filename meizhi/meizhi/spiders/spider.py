import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from meizhi.items import MeizhiItem
import random

import meizhi.zhihuLogIn
from meizhi.zhihuLogIn import isLogin,login
import requests
try:
	import cookielib
except:
	import http.cookiejar as cookielib
import time
import os.path
try:
	from PIL import Image
except:
	pass

class Spider(scrapy.Spider):
	
	# 构造 Request headers
	agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding": "gzip,deflate",
		"Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
		"Connection": "keep-alive",
		"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/48.0.2564.97 Safari/537.36",
		"Referer": "http://www.zhihu.com"
	}

	# 使用登录cookie信息
	session = requests.session()
	session.cookies = cookielib.LWPCookieJar(filename='cookies')
	try:
		session.cookies.load(ignore_discard=True)
	except:
		print("Cookie 未能加载")

	name = "meizhi"
	allow_domains = ["https://www.zhihu.com/"]
	start_url_head = "https://www.zhihu.com/collection/38624707?page=1"
	
	# def __init__(self, *args, **kwargs):
		# super(Spider, self).__init__(*args, **kwargs)
		# self.xsrf = ''
		
	def start_requests(self):
		if isLogin():
			print ('you have already loged in')
			yield meizhi.zhihuLogIn.session.get(self.start_url_head, self.after_login)

		else:
			account = input('请输入你的用户名\n>  ')
			secret = input("请输入你的密码\n>	")
			login(secret, account)
			print ('ok,now you are loged in')
			
			yield session.get(self.start_url_head, callback = self.after_login)
			
		
	def after_login(self, response):
		pirnt('you are in the after_login')

		
	def parse_firstpage(self,response):
		print ('get in the parse_firstpage')
		exit(0)
		
		
	def parse_err(self, response):
		log.ERROR('crawl {} failed'.format(response.url))
		
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