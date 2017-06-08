# zhihu_class.py
from global_class import *
# import global_class
from bs4 import BeautifulSoup  
import re
from urllib.error import URLError
import time
import lxml
from lxml import etree
class zhihu_class:
	def __init__(self):
		self.glb = global_class()
		self.headers = {
    "Host": "www.zhihu.com",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
		}


	def GetSinglePageAllPics(self, url, intPage):

		strPathNameHeader = self.glb.GetSysPlat()
		
		# print("self.headers: ", glb.headers)
		lstThisPageSrcs = self.GetSinglePageCollectionSrc(url)

		for address in lstThisPageSrcs:  
			if(address != None):	
				strName = str(intPage) + "_" + str(self.glb.count)
				strFullPath = strPathNameHeader + strName +".jpg"
				# print("strFullPath: ", strFullPath)
				# exit()
				#设置路径和文件名	
				print ("正在下载: ", strName)
				self.glb.DownLoadInBinary(address,strFullPath)#下载 
				self.glb.count = self.glb.count + 1#计数君+1


	def GetSinglePageCollectionSrc(self, collectionPageUrl):
		req = requests.request("GET", collectionPageUrl, headers = self.headers)
		if req.status_code != 200:
			print("bad req in single page: ", req.status_code)

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
				reqAnswer = requests.request("GET", addressLinkFull, headers = self.headers)
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

	def IsPageTailExist(self, urlCollection):
		if urlCollection.find("page") == -1:
			return True
		else:
			return False

	def GetTotalPageNum(self, urlCollection):
		req = requests.get(urlCollection, headers = self.headers)
		soup = BeautifulSoup(req.content, "html")
		# html = lxml.etree.parse(req.text)
		nodeNextPage = soup.find(text = "下一页").find_previous()
		print("nodeNextPage: ", nodeNextPage)
		nodeLastPage = nodeNextPage.find_previous().find_previous()
		print("nodeLastPage: ", nodeLastPage)
		totalPageNum = nodeLastPage.text
		print("totalPageNum: ", totalPageNum)
		# exit()
		return totalPageNum

