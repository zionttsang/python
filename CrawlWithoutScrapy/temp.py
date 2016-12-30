
import zhihuLogIn
import tt
import globalClass
import urllib.request
from bs4 import BeautifulSoup
import globalClass

urlOrigin = ""
urlFirst = "https://www.zhihu.com/collection/60771406?page="

def main(url):
	if zhihuLogIn.isLogin():
		print('您已经登录')
		
		for i in range(50):
			urlTemp = urlFirst + str(i+1)
			print("urlTemp: ",urlTemp)
			
			tt.AfterLogIn(urlTemp,i)
	else:
		account = input('请输入你的用户名\n>  ')
		secret = input("请输入你的密码\n>	")
		zhihuLogIn.login(secret, account)
		
if __name__ == '__main__':
	main(urlFirst)