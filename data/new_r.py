import re
import os
import cv2


width = 600
height = 600
dim = (width, height)

i = 210
for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		#print(os.path.join(root, name))
		nameImage = os.path.join(root,name)
		nameImage = str(nameImage)
		name_root = str(root)
		if re.search(r'annotation_test',nameImage):
			print(nameImage)
			if re.search(r'.xml',nameImage):
				os.rename(nameImage,str(i)+".xml")
				i = i + 1
				print("+")

