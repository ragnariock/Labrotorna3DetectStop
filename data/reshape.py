import re
import os
import cv2

num = 210

width = 600
height = 600
dim = (width, height)


for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		#print(os.path.join(root, name))
		nameImage = os.path.join(root,name)
		nameImage = str(nameImage)
		name_root = str(root)
		if re.search(r'images_test',name_root):
			if (r'jpg',nameImage ) or re.search(r'jpeg',nameImage) or re.search(r'png',nameImage) or re.search(r'JPG',nameImage):
				img = cv2.imread(nameImage)

				resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

				cv2.imwrite('test/'+str(num) + '.jpg', resized )
				num +=1

print(num)
