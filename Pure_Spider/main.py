
# import zhihuLogIn
# import main_brain
from multiprocessing import Process, Lock
import string
import global_class
from zhihu_class import *
import sys

# https://www.zhihu.com/collection/119998384

cZhi = zhihu_class()

def main(collectionUrl):
	# check page tail
	if cZhi.IsPageTailExist(collectionUrl) == False:
		print("Wrong Collection Url")
		exit()
	pageTail = "?page="
	urlCollectionWithPageTail = collectionUrl + pageTail
	print(urlCollectionWithPageTail)

	# check total page num
	totalPageNum = cZhi.GetTotalPageNum(collectionUrl)
	processNum = int((int(totalPageNum) / 10) + 1)
	print("processNum: ", processNum)
	for i in range(processNum):
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

	main(sys.argv[1])
	# print("sys.argv: ",sys.argv[1], sys.argv[2])