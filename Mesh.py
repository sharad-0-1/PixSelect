import cv2
from os import listdir

names = listdir("imag")
image_ = []
color_ = []
for k in range(len(names)):
	image_.append(cv2.resize(cv2.imread("imag/"+ names[k]),(60,60)))
	color_.append(cv2.mean(image_[k]))
test = cv2.imread("test.jpg")
w, h, c = test.shape
test = cv2.resize(test,((h//12 + 1)*120, (w//12 + 1)*120))
h, w, c = test.shape
print(test.shape)
p,q = 0,0
for i in range(60,h+1,60):
	q = 0
	print(i)
	for j in range(60,w+1,60):
		color = cv2.mean(test[p:i , q:j])
		image = cv2.resize(cv2.imread("imag/0_2000.jpg"),(60,60))
		color1 = cv2.mean(image)
		diff = pow(pow(color1[0]-color[0],2)+pow(color1[1]-color[1],2)+pow(color1[2]-color[2],2),1/2)
		for k in range(len(names)):
			color1 = color_[k]
			diff1 = pow(pow(color1[0]-color[0],2)+pow(color1[1]-color[1],2)+pow(color1[2]-color[2],2),1/2)
			if(diff1 <diff):
				diff = diff1
				image = image_[k]
		for ii in range(p,i):
			for jj in range(q,j):
				test[ii,jj] = image[ii-p, jj-q]
		q = j
	p = i
cv2.imshow("image", test)
cv2.imwrite("image4.jpg",test)
cv2.waitKey(0)