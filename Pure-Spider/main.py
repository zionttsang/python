
# import zhihuLogIn
import main_brain
import urllib.request
from bs4 import BeautifulSoup
import globalClass

# urlFirst = "https://www.zhihu.com/collection/60771406?page=" #daxiong
urlFirst = "https://www.zhihu.com/collection/38624707?page=" #baozhao
pageNum = 67

def main(url):
	
	# ==============
	# Log in Version
	# ==============
	# if zhihuLogIn.isLogin():
	# 	print('您已经登录')
		
	# 	for i in range(pageNum):
	# 		urlTemp = urlFirst + str(i+1)
	# 		print("urlTemp: ",urlTemp)
			
	# 		Main-Brain.AfterLogIn(urlTemp)
	# else:
	# 	account = input('请输入你的用户名\n>  ')
	# 	secret = input("请输入你的密码\n>	")
	# 	zhihuLogIn.login(secret, account)

	# ============
	# Easy Version
	# ============

	for i in range(pageNum):
		print("Page: ", i + 1)
		urlThisPage = urlFirst + str(i + 1)
		main_brain.GetAllPics(urlThisPage)

		
if __name__ == '__main__':
	main(urlFirst)