
import requests
from bs4 import BeautifulSoup
import os
import re
import time
from urllib.request import urlopen
from urllib.error import URLError
from tsangLibs.globalClass import *
from tsangLibs.webDriver import *

# meta elements
start_url = "https://www.zhihu.com/collection/38624707?page=1"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
count = globalClass()

def GetAllTheLinksOfCollection(url):

	print ("we are in the func now")
	resPage = requests.get(url, headers = headers)#打开目标地址
	print (resPage.status_code)

	soup=BeautifulSoup(resPage.text)#实例化一个BeautifulSoup对象	 
	lstImg = []#Create listImg Obj
	  
	print("prepare for the loop")
	
	for link in soup.find_all("link",href = re.compile("answer")):#获取标签为link的内容	

		print ("link: ",link)
	
		addressLink=link.get("href")#获取标签属性为href的内容，即该回答的地址			
		print("addressLink:",addressLink)
		
		addressLinkFull = "https://www.zhihu.com" + addressLink
		print ("adressLinkFull: ",addressLinkFull) 
			
		try:
			resAnswer = requests.get(addressLinkFull, headers = headers)
			time.sleep(1)
		except URLError as e:
			print("bad path!!")
			print(e.reason)
			continue
		
		soupAnswer = BeautifulSoup(resAnswer.text)
		
		for linkImg in soupAnswer.find_all("img"):
			addressImg = linkImg.get("data-original")
			lstImg.append(addressImg)

	s = set(lstImg)
	# print ("get all the img_links,pause")
	# exit(0)
	

	for address in s:  
		if(address!=None):	
			pathName="E:\\2666\\"+ str(count.z) +".jpg"#设置路径和文件名	
			download(address,pathName)#下载 
			print ("正在下载第：",count.z)			
			count.z=count.z+1#计数君+1

def NextPage():
	ObjDriver = webDriver()
	driver = webDriver.driver
	driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[3]/div/span[8]/a/@[href]").click()
	time.sleep(5) # 控制间隔时间，等待浏览器反映
	nextPageUrl = driver.current_url
	GetAllTheLinksOfCollection(nextPageUrl)



def download(_url,name):#下载函数  
	if(_url==None):#地址若为None则跳过	 
		pass  
	resDown = requests.get(_url,headers = headers)#打开链接  
	# time.sleep(0.25) # 时间间隔为0.5s发送一次抓取请求，减轻hoj服务器压力
	# resTest = urlopen(_url)
	# print ("test: ", resDown.text.encoding("gbk","ignore"))
	# print ("resDown.content: ", resDown.content)
	# exit(0)
	if (resDown.status_code == 200):
		data=resDown.content #否则开始下载到本地  
		with open(name, "wb") as code:
			code.write(data)
			code.close()
	else:
		print("resDown get error!")

if __name__ == "__main__":

	GetAllTheLinksOfCollection(start_url)