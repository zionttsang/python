
#coding=utf-8  
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup  
import requests
import os  
import re
import platform
# from zhihuLogIn import isLogin,login
from globalClass import *
import time

#urlFirst = "https://www.zhihu.com/collection/60771406?page=1"#指定的URL
glb = globalClass()
strPathNameHeader = ""

agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    'User-Agent': agent
}

def GetAllPics(url):

	strPathNameHeader = GetSysPlat()
	# print("Header: ", strPathNameHeader)
	# exit()


	req = requests.request("GET", url, headers = headers)
	print("status code: ", req.status_code)
	soup=BeautifulSoup(req.content,"lxml")\

	lstImg = []#Create listImg Obj
		
	print("prepare for the loop")
	
	for link in soup.find_all("link",href = re.compile("answer")):#获取标签为link的内容	

		print ("link: ",link)
	
		addressLink=link.get("href")#获取标签属性为href的内容，即该回答的地址			
		print("addressLink:",addressLink)
		
		addressLinkFull = "https://www.zhihu.com" + addressLink
		print ("adressLinkFull: ",addressLinkFull) 
			
		try:
			reqAnswer = requests.request("GET", addressLinkFull, headers = headers)
			time.sleep(1)
		except URLError as e:
			print("bad path!!")
			print(e.reason)
			continue
		
		# respondImg = reqAnswer.read()
		# reqAnswer.close()
		soupImg = BeautifulSoup(reqAnswer.content, "lxml")
		
		for linkImg in soupImg.find_all("img"):
			addressImg = linkImg.get("data-original")
			lstImg.append(addressImg)

	lstThisPageSrcs = set(lstImg)
	

	for address in lstThisPageSrcs:  
		if(address != None):	
			strFullPath = strPathNameHeader + str(glb.count) +".jpg"
			# print("strFullPath: ", strFullPath)
			# exit()
			#设置路径和文件名	
			download(address,strFullPath)#下载 
			print ("正在下载第：",glb.count)			
			glb.count = glb.count + 1#计数君+1


def download(_url,name):#下载函数  
	if(_url==None):#地址若为None则跳过	 
		pass  
	resDown = urlopen(_url)#打开链接  
	# time.sleep(0.25) # 时间间隔为0.5s发送一次抓取请求，减轻hoj服务器压力
	if (resDown.getcode() == 200):
		data=resDown.read()#否则开始下载到本地  
		resDown.close()
		with open(name, "wb") as code:
			code.write(data)
			code.close()
	else:
		print("resDown get error!")
		resDown.close()


def GetSysPlat():
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


import os, sys

if __name__ == "__main__":
	dir = input("dir:")
	
	dir_list = os.listdir(dir)
	for this_dir in dir_list:
		# if os.path.isdir(this_dir):
			# print("this dir:",this_dir)
			this_dir = dir + this_dir
			print("this dir:",this_dir.encode("gbk","ignore"))
			try:
				os.removedirs(this_dir)
				print(this_dir,"has been removed")
			except:
				print("this dir is not empty or not a dir")
				pass
		# else:
			# continue
			

