import cv2
from os import listdir

names = listdir("images")
image_ = [[cv2.imread("images/"+ names[0])]]
cv2.imwrite("img/images/"+names[0],image_[0][0])
color_ = [[round(i)//10 for i in cv2.mean(image_[0][0])]]
i = 1
for nm in names[1:]:
	img = cv2.imread("images/"+ nm)
	clr = [round(i)//10 for i in  cv2.mean(img)]
	if(img is None or img.shape[0] < 55 or (clr in color_)):
		print("same")
		pass
	else:
		image_.append([img])
		cv2.imwrite("img/images/"+nm,img)
		print(clr)
		color_.append(clr)
		i += 1