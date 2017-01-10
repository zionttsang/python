
import zhihuLogIn
import tt
import urllib.request
from bs4 import BeautifulSoup
import globalClass

# urlFirst = "https://www.zhihu.com/collection/60771406?page=" #daxiong
urlFirst = "https://www.zhihu.com/collection/38624707?page=" #baozhao
pageNum = 67

def main(url):
	
	if zhihuLogIn.isLogin():
		print('您已经登录')
		
		for i in range(pageNum):
			urlTemp = urlFirst + str(i+1)
			print("urlTemp: ",urlTemp)
			
			tt.AfterLogIn(urlTemp)
	else:
		account = input('请输入你的用户名\n>  ')
		secret = input("请输入你的密码\n>	")
		zhihuLogIn.login(secret, account)
		
if __name__ == '__main__':
	main(urlFirst)