
# from scrapy.cmdline import execute
# execute(["scrapy","crawl","meizhi"])

# import requests
# from requests.packages import urllib3 

# urllib3.disable_warnings()
# response = requests.get("https://www.12306.cn",verify = False)
# print (response.status_code)

from urllib import request

req = request.Request('http://www.baidu.com/')
res = request.urlopen(req)
print ("res code:",res.getcode())