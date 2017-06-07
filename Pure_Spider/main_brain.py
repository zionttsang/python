
#coding=utf-8  
# from zhihuLogIn import isLogin,login
from global_class import *
from zhihu_class import *
import time

#urlFirst = "https://www.zhihu.com/collection/60771406?page=1"#指定的URL
glb = global_class()
cZhi = zhihu_class()

def GetSinglePageAllPics(url, intPage):

	strPathNameHeader = glb.GetSysPlat()
	
	# print("self.headers: ", glb.headers)
	lstThisPageSrcs = cZhi.GetSinglePageCollectionSrc(url)	

	for address in lstThisPageSrcs:  
		if(address != None):	
			strName = str(intPage) + "_" + str(glb.count)
			strFullPath = strPathNameHeader + strName +".jpg"
			# print("strFullPath: ", strFullPath)
			# exit()
			#设置路径和文件名	
			print ("正在下载: ", strName)
			glb.DownLoadInBinary(address,strFullPath)#下载 
			glb.count = glb.count + 1#计数君+1


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
			

