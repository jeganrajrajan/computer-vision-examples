import cv2
# load the image, display it to our screen, and initialize a list of
# kernel sizes (so we can evaluate the relationship between kernel
# size and amount of blurring)
img = cv2.imread(r"D:\computer_vision\data\hat_ex.png")
image =cv2.resize(img,(0,0),fx =0.5,fy=0.5,interpolation =cv2.INTER_AREA)
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]
# loop over the kernel sizes
# for (kX, kY) in kernelSizes:
# 	# apply an "average" blur to the image using the current kernel
# 	# size
# 	blurred = cv2.blur(image, (kX, kY))
# 	cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
# 	cv2.waitKey(0)
# Gussianblur
# loop over the kernel sizes again
# for (kX, kY) in kernelSizes:
# 	# apply a "Gaussian" blur to the image
# 	blurred = cv2.GaussianBlur(image, (kX, kY), 0)
# 	cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
# 	cv2.waitKey(0)
# medianblur
# for k in (3, 9, 15):
# 	# apply a "median" blur to the image
# 	blurred = cv2.medianBlur(image, k)
# 	cv2.imshow("Median {}".format(k), blurred)
# 	cv2.waitKey(0)

# bilateralFilter
img1 = cv2.imread(r'D:\computer_vision\data\taj_bilatral.jpg')
params = [(11, 21, 7), (11, 41, 21), (15, 75, 75)]
# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering to the image using the current set of
	# parameters
	blurred = cv2.bilateralFilter(img1, diameter, sigmaColor, sigmaSpace)
	# show the output image and associated parameters
	title = "Blurred d={}, sc={}, ss={}".format(
		diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)