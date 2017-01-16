
#coding=utf-8  
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup  
import os  
import re	
from zhihuLogIn import isLogin,login
from globalClass import *
import time

#urlFirst = "https://www.zhihu.com/collection/60771406?page=1"#指定的URL
count = globalClass()
  
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

def AfterLogIn(url):

	print('start AfterLogIn')
	
	resPage = urlopen(url)#打开目标地址  
	respond=resPage.read()#获取网页地址源代码  
	resPage.close()

	soup=BeautifulSoup(respond,"lxml")#实例化一个BeautifulSoup对象	 
	lstImg = []#Create listImg Obj
	  
	print("prepare for the loop")
	
	for link in soup.find_all("link",href = re.compile("answer")):#获取标签为link的内容	

		print ("link: ",link)
	
		addressLink=link.get("href")#获取标签属性为href的内容，即该回答的地址			
		print("addressLink:",addressLink)
		
		addressLinkFull = "https://www.zhihu.com" + addressLink
		print ("adressLinkFull: ",addressLinkFull) 
			
		try:
			reqAnswer = urlopen(addressLinkFull)
		except URLError as e:
			print("bad path!!")
			print(e.reason)
			continue
		
		respondImg = reqAnswer.read()
		reqAnswer.close()
		soupImg = BeautifulSoup(respondImg)
		
		for linkImg in soupImg.find_all("img"):
			addressImg = linkImg.get("data-original")
			lstImg.append(addressImg)

	s = set(lstImg)
	

	for address in s:  
		if(address!=None):	
			pathName="E:\\2666\\"+ str(count.z) +".jpg"#设置路径和文件名	
			download(address,pathName)#下载 
			print ("正在下载第：",count.z)			
			count.z=count.z+1#计数君+1
			

import os, sys

if __name__ == "__main__":
	dir = input("dir:")
	
	dir_list = os.listdir(dir)
	for this_dir in dir_list:
		# if os.path.isdir(this_dir):
			# print("this dir:",this_dir)
			this_dir = dir + this_dir
			try:
				os.removedirs(this_dir)
				print(this_dir,"has been removed")
			except:
				print("i dont think i can show up")
				pass
		# else:
			# continue
			

