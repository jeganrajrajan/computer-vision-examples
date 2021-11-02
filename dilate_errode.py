# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np

# Reading the input image
# img = cv2.imread(r'D:\computer_vision\data\flower.jpeg', 0)
#
# # Taking a matrix of size 5 as the kernel
# kernel = np.ones((5, 5), np.uint8)
#
# # The first parameter is the original image,
# # kernel is the matrix with which image is
# # convolved and third parameter is the number
# # of iterations, which will determine how much
# # you want to erode/dilate a given image.
# img_erosion = cv2.erode(img, kernel, iterations=1)
# img_dilation = cv2.dilate(img, kernel, iterations=1)
#
# cv2.imshow('Input', img)
# cv2.imshow('Erosion', img_erosion)
# cv2.imshow('Dilation', img_dilation)
#
# cv2.waitKey(0)

# opening&closing
image = cv2.imread(r"D:\computer_vision\data\morphology_ex.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernelSizes = [(3, 3), (5, 5), (7, 7)]
# loop over the kernels sizes
for kernelSize in kernelSizes:
    # construct a rectangular kernel from the current size and then
    # apply an "opening" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(
        kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)

# closing
for kernelSize in kernelSizes:
    # construct a rectangular kernel form the current size, but this
    # time apply a "closing" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(
        kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

# Gradient
image = cv2.imread(r"D:\computer_vision\data\flower.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for kernelSize in kernelSizes:
    # construct a rectangular kernel and apply a "morphological
    # gradient" operation to the image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(
        kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)

# Morphological hat
image = cv2.imread(r"D:\computer_vision\data\hat_ex.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# construct a rectangular kernel (13x5) and apply a blackhat
# operation which enables us to find dark regions on a light
# background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
# show the output images
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)

#  regions that are light against a dark background are clearly displayed — in this case, we can clearly see that the license plate region of the car has been revealed.
# But also note that the license plate characters themselves have not been included. This is because the license plate characters are dark against a light background.