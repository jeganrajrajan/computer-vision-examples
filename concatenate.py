import numpy
import cv2
img = cv2.imread(r'D:\computer_vision\data\image1.jpg')
verticalAppendedImg = numpy.vstack((img,img))
horizontalAppendedImg = numpy.hstack((img,img,img))

cv2.imshow('Vertical Appended', verticalAppendedImg)
cv2.imshow('Horizontal Appended', horizontalAppendedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

# colorspace images
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayImageBGRspace = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

horizontalAppendedIGrayImg = numpy.hstack((img, grayImageBGRspace))

cv2.imshow('Horizontal Appended Gray Img', horizontalAppendedIGrayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()