import requests
import platform

class global_class:
	def __init__(self):
		self.count = 1

		self.headers = {
    "Host": "www.zhihu.com",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
		}

	def GetSysPlat(self):
		# print ("init with sys")

		strSystem = platform.system()
		print(strSystem)
		if (strSystem == "Windows"):
			# self.driver = webdriver.PhantomJS(executable_path = "D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe") 
			strPathNameHeader = "E:\\2666\\"
		else:
			# self.driver = webdriver.PhantomJS(executable_path = "/Volumes/apple hdd/phantomjs-2.1.1-macosx/bin/phantomjs")

			strPathNameHeader = "/Volumes/apple hdd/Github/python/Pure_Spider/2666/"

		return strPathNameHeader

	def DownLoadInBinary(self, url, fullPath):
		if(url==None):#地址若为None则跳过	 
			pass  
		resDown = requests.get(url)#打开链接  
		# time.sleep(0.25) # 时间间隔为0.5s发送一次抓取请求，减轻hoj服务器压力
		if (resDown.status_code == 200):
			data=resDown.content#否则开始下载到本地  
			with open(fullPath, "wb") as code:
				code.write(data)
		else:
			print("resDown get error!")