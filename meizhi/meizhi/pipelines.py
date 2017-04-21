# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from meizhi import settings
import os
import time
from meizhi import globalClass

class meizhiPipeline(object):

	count = globalClass.get_count()
	
	def process_item(self, item, spider):
		print ("we are in the pipe now")
		dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)			

		if not os.path.exists(dir_path):
			os.makedirs(dir_path)
		for image_url in item['image_urls']:
			
			res = requests.get(image_url)
			time.sleep(1)

			if (res.status_code == 200):
				binary_img = res.content
				file_path = dir_path + str(count.z) + ".jpg"
				count.z = count.z + 1
				with open(file_path, "wb") as handle:
					handle.write(binary_img)
					handle.close()
			else:
				print("bad image url")
				pass
			
		return item
			# with open(file_path, 'wb') as handle:
			# 	image = requests.get(image_url, stream=True)
			# 	for block in response.iter_content(1024):
			# 		if not block:
			# 			break

			# 		handle.write(block)

			# item['images'] = images
		
