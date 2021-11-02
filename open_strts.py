import cv2
import numpy as np
open_img = cv2.imread(r"D:\computer_vision\data\banner.png")
print(open_img)
cv2.imshow('sample image', open_img)

cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image

cv2.imwrite('test.png',open_img)

# get dimensions of image
dimensions = open_img.shape

# height, width, number of channels in image
height = open_img.shape[0]
width = open_img.shape[1]
channels = open_img.shape[2]
# colour_channels
nemo = cv2.imread(r'D:\computer_vision\data\nemo.jpg')
blue, green, red = cv2.split(nemo)
zeros = np.zeros(blue.shape,np.uint8)
blue_merge = cv2.merge((blue,zeros,zeros))
clr_img = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)

# resize
img = cv2.imread(r'D:\computer_vision\data\excel-invoice-template.png')

print('Original Dimensions : ', img.shape)

scale_percent = 220  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# change either width or height
img1 = cv2.imread(r'D:\computer_vision\data\excel-invoice-template.png')

print('Original Dimensions : ', img1.shape)

width = 440
height = img1.shape[0]  # keep original height
dim = (width, height)

# resize image
resized1 = cv2.resize(img1, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized1.shape)

cv2.imshow("Resized image", resized1)
cv2.waitKey(0)
cv2.destroyAllWindows()