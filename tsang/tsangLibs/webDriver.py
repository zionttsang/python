
from selenium import webdriver

class WebDriver():
	def __init__(self):
		# self.driver = webdriver.PhantomJS(executable_path = "D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe") 

		self.driver = webdriver.PhantomJS(executable_path = "/Volumes/apple hdd/phantomjs-2.1.1-macosx/bin/phantomjs")		
	# def __del__(self):
	# 	self.driver.close()
		
if __name__ == "__main__":
	print ("webDriver module")