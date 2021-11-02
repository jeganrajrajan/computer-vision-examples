import cv2
import numpy as np

img = cv2.imread(r"D:\computer_vision\data\A._P._J._Abdul_Kalam.jpg")
dim = (500,500)
image = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
# cv2.imshow("Original", image)

# a mask is the same size as our image, but has only two pixel
# values, 0 and 255 -- pixels with a value of 0 (background) are
# ignored in the original image while mask pixels with a value of
# 255 (foreground) are allowed to be kept
# mask = np.zeros(image.shape[:2], dtype="uint8")
# cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
# cv2.imshow("Rectangular Mask", mask)
#
# # apply our mask -- notice how only the person in the image is
# # cropped out
# masked = cv2.bitwise_and(image, image, mask=mask)
# cv2.imshow("Mask Applied to Image", masked)
# cv2.waitKey(0)


# now, let's make a circular mask with a radius of 100 pixels and
# apply the mask again
# mask = np.zeros(image.shape[:2], dtype="uint8")
# cv2.circle(mask, (145, 200), 100, 255, -1)
# masked = cv2.bitwise_and(image, image, mask=mask)
# # show the output images
# cv2.imshow("Circular Mask", mask)
# cv2.imshow("Mask Applied to Image", masked)
# cv2.waitKey(0)

# Python program to explain
# mask inversion on a RGB image.

# invert image

# Reading an image
img = cv2.imread(r'D:\computer_vision\data\apple_image.jpg')

# The kernel to be used for dilation
# purpose
kernel = np.ones((5, 5), np.uint8)

# converting the image to HSV format
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# defining the lower and upper values
# of HSV, this will detect yellow colour
Lower_hsv = np.array([20, 70, 100])
Upper_hsv = np.array([30, 255, 255])

# creating the mask
Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)

# Inverting the mask
mask_yellow = cv2.bitwise_not(Mask)
Mask = cv2.bitwise_and(img, img, mask = mask_yellow)

# Displaying the image
cv2.imshow('Mask', Mask)

# waits for user to press any key
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
