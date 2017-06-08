
# import zhihuLogIn
import main_brain
from multiprocessing import Process, Lock
import string
import global_class

class main():
	def __init__(self, collectionUrl, pageNum):
	# urlFirst = "https://www.zhihu.com/collection/60771406?page=" #daxiong
		self.collectionUrl = collectionUrl
		self.pageNum = pageNum

	def main(self):

		# print("Page/s: ", int(pageNum / 10))
		for i in range(int(self.pageNum / 10) + 1):
			p = Process(target = self.SingleProcess, args = (i,))
			p.start()

	def SingleProcess(self, i):
		print("Process Num: ", i)
		for j in range(10):
			if i != 0:
				intPage = str((i*10) + j)
				urlThisPage = self.collectionUrl + str((i*10) + j)
			else:
				if j == 9:
					continue
				intPage = str(j + 1)
				urlThisPage = self.collectionUrl + str(j + 1)

			print("urlThisPage: ",urlThisPage)
			# continue
			main_brain.GetSinglePageAllPics(urlThisPage, intPage)
			# time.sleep(1)
		
if __name__ == '__main__':
	collectionUrl = "https://www.zhihu.com/collection/38624707?page=" #baozhao
	pageNum = 67
	cMain = main(collectionUrl, pageNum)
	cMain.main()