
import requests
import requests.packages.urllib3.util.ssl_ 
from bs4 import BeautifulSoup
import os
import re
import time
# from urllib.request import urlopen
from urllib.error import URLError
from tsangLibs.GlobalClass import *
from tsangLibs.WebDriver import *

# meta elements
# start_url = "https://www.zhihu.com/collection/38624707?page=1"
start_url = "https://www.zhihu.com/collection/41659037"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
count = GlobalClass()
# In case of SSLV3_HANDSHAKE_FAILURE
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

ObjDriver = WebDriver()
driver = ObjDriver.driver

def GetAllTheImagesOfCollection(url):

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
			# pathName="F:\\2666\\"+ str(count.z) +".jpg"#设置路径和文件名
			pathName="/Volumes/apple hdd/2666/"+ str(count.z) +".jpg"#设置路径和文件名
			download(address,pathName)#下载 
			print ("正在下载第：",count.z)			
			count.z=count.z+1#计数君+1

	driver.get(url)
	countCurrentUrl = driver.current_url
	print("Finished with this Page: ",countCurrentUrl,"\n\n")
	# exit(0)
	NextPage(url)

def NextPage(usedUrl):
	# driver.find_element_by_link_text("下一页").click()
	driver.find_element_by_xpath("//a[contains(text(),'下一页')]").click()
	time.sleep(4) # 控制间隔时间，等待浏览器反映
	nextPageUrl = driver.current_url
	if usedUrl == nextPageUrl:
		print ("No more new pages or Click failed")
		exit(0)
	else:
		print ("Now we crawl new Page: ",driver.current_url)
		GetAllTheImagesOfCollection(nextPageUrl)
	


	# /html/body/div[3]/div[1]/div/div[3]/div/span[9]/a
	# /html/body/div[3]/div[1]/div/div[3]/div/span[10]/a
	# /html/body/div[3]/div[1]/div/div[3]/div/span[11]/a

def download(_url,name):#下载函数  
	if(_url==None):#地址若为None则跳过	 
		pass  
	resDown = requests.get(_url,headers = headers)#打开链接  
	time.sleep(0.4) # 时间间隔为0.5s发送一次抓取请求，减轻hoj服务器压力
	if (resDown.status_code == 200):
		data=resDown.content #否则开始下载到本地  
		with open(name, "wb") as code:
			code.write(data)
			code.close()
	else:
		print("resDownload get error!")

if __name__ == "__main__":

	GetAllTheImagesOfCollection(start_url)