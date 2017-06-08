
# import zhihuLogIn
import main_brain
from multiprocessing import Process, Lock
import string
import global_class
from zhihu_class import *
import sys

# class main():
# 	def __init__(self, collectionUrl, pageNum):
# 	# urlFirst = "https://www.zhihu.com/collection/60771406?page=" #daxiong
# 		self.collectionUrl = collectionUrl
# 		self.pageNum = pageNum
cZhi = zhihu_class()

def main(collectionUrl, pageNum):
	# check page tail
	if cZhi.IsPageTailExist(collectionUrl) == False:
		print("Wrong Collection Url")
		exit()
	pageTail = "?page="
	urlCollectionWithPageTail = collectionUrl + pageTail
	print(urlCollectionWithPageTail)

	# check total page num
	totalPageNum = cZhi.GetTotalPageNum(collectionUrl)

	for i in range(int((int(pageNum) / 10) + 1)):
		p = Process(target = SingleProcess, args = (urlCollectionWithPageTail, i,))
		p.start()

def SingleProcess(collectionUrl, i):
	print("Process Num: ", i)
	for j in range(10):
		if i != 0:
			intPage = str((i*10) + j)
			urlThisPage = collectionUrl + str((i*10) + j)
		else:
			if j == 9:
				continue
			intPage = str(j + 1)
			urlThisPage = collectionUrl + str(j + 1)

		print("urlThisPage: ",urlThisPage)
		# continue
		cZhi.GetSinglePageAllPics(urlThisPage, intPage)
		# time.sleep(1)
		
if __name__ == '__main__':

	main(sys.argv[1], sys.argv[2])
	# print("sys.argv: ",sys.argv[1], sys.argv[2])