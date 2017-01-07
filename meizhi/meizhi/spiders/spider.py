import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from meizhi.items import MeizhiItem
import random

import meizhi.zhihuLogIn
from meizhi.zhihuLogIn import isLogin,login,get_session

class Spider(scrapy.Spider):
	
	# 构造 Request headers
	# headers = {
		# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		# 'Accept-Encoding':'gzip, deflate, sdch, br',
		# 'Accept-Language':'zh-CN,zh;q=0.8',
		# 'Connection':'keep-alive',
		# 'Cache-Control':'max-age=0'
		# ,'Host':'www.zhihu.com'
		# ,'Upgrade-Insecure-Requests':'1'
		# ,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
	# }

	name = "meizhi"
	allow_domains = ["https://www.zhihu.com/"]
	start_url_head = "https://www.zhihu.com/collection/38624707?page=1"
		
	def start_requests(self):
		if meizhi.zhihuLogIn.isLogin:
			print ("you have loged in")
			_s = get_session
			cookie = _s.cookies
			return Request(start_url_head,cookie,callback = after_login)
		else:
			print ("you should log in now")
			
	def post_login(self, response):
		pirnt('Preparing login')
		xsrf = Selector(response).xpath('//input[@name = "_xsrf"]/@value').extract()[0]
		print (xsrf)
		
		return FormRequest.from_response(response, #'http://www.zhihu.com/#signin'
							meta = {"cookiejar" : 1},
							headers = self.headers,
							formdata = {
							'_xsrf' : xsrf,
							'email' : 'zeta221@163.com',
							'password' : 'cdefgab',
							'remember_me' : 'true'
							},
							callback = self.after_login,
							)

		
	def after_login(self,response):
		print ('get in the after_signin')
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