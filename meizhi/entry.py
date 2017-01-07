
# from scrapy.cmdline import execute
# execute(["scrapy","crawl","meizhi"])

# import requests
# from requests.packages import urllib3 

# urllib3.disable_warnings()
# response = requests.get("https://www.12306.cn",verify = False)
# print (response.status_code)

import requests,os

class test():
	def __init__(self):
		self.print_what_i_need()

	def print_what_i_need(self):
		print ("i have get in what i need")
		
if __name__ == "__main__":
	z = test()