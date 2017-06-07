# zhihu_class.py
from global_class import *
from bs4 import BeautifulSoup  
import re
from urllib.error import URLError
import time

class zhihu_class:
	def __init__(self):
		self.glb = global_class()

	def GetSinglePageCollectionSrc(self, collectionPageUrl):
		req = requests.request("GET", collectionPageUrl, headers = self.glb.headers)
		if req.status_code != 200:
			print("bad req in single page: ", req.status_code)
			return False
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
				reqAnswer = requests.request("GET", addressLinkFull, headers = self.glb.headers)
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

		return set(lstImg)
