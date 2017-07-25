import requests
import platform
import os

class global_class:
	def __init__(self):
		self.count = 1

		# self.headers = {
  #   "Host": "www.zhihu.com",
  #   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
		# }

	def GetSysPlat(self):
		# print ("init with sys")

		strSystem = platform.system()
		print(strSystem)
		if (strSystem == "Windows"):
			dir_path = "E:\\2666\\"
			if not os.path.exists(dir_path):
				os.makedirs(dir_path)
			strPathNameHeader = "E:\\2666\\"

		elif(strSystem == "Linux"):
			dir_path = "/home/tsang/Desktop/2666/"
			if not os.path.exists(dir_path):
				os.makedirs(dir_path)
			strPathNameHeader = "/home/tsang/Desktop/2666/"
		else:
			dir_path = "/Volumes/apple hdd/2666/2666/"
			if not os.path.exists(dir_path):
				os.makedirs(dir_path)
			strPathNameHeader = "/Volumes/apple hdd/2666/2666/"

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