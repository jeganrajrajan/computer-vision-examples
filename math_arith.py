import cv2
import numpy as np

image1 = cv2.imread(r'D:\computer_vision\data\image1.jpg')
image2 = cv2.imread(r"D:\computer_vision\data\image2.jpg")

add_img = image1 +image2
add_img1 = cv2.add(image1,image2)
cv2.imshow('add_img',add_img)
cv2.imshow('default add function',add_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
sub_img = image1-image2
sub_img2 = cv2.subtract(image1,image2)
cv2.imshow('sub_img',sub_img)
cv2.imshow('sub_img1',sub_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


multi_img = image1*image2
multi_img1 = cv2.multiply(image1,image2)
cv2.imshow('multi_img',multi_img)
cv2.imshow('multi_img1',multi_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

div_img = image1/image2
div_img1 = cv2.divide(image1,image2)
cv2.imshow('div_img',div_img)
cv2.imshow('div1_img1',div_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()