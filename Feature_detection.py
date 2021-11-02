import cv2
import numpy as np
import imutils
from skimage.feature import hog

input_img = r'D:\computer_vision\data\tajmahal.jpg'
dim = (500,500)

# ori = cv2.imread(input_img)
image = cv2.imread(input_img)
imput_img = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
ori = imput_img.copy()
gray = cv2.cvtColor(imput_img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
imput_img[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow('Original',ori)
cv2.imshow('Harris',imput_img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# Shi-Tomasi

img1 = cv2.imread(r'D:\computer_vision\data\tajmahal.jpg')
img = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
ori = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,20,0.01,10)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
cv2.imshow('Original', ori)
cv2.imshow('Shi-Tomasi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# sift
img1 = cv2.imread(r'D:\computer_vision\data\tajmahal.jpg')
img = cv2.resize(img1,dim,interpolation=cv2.INTER_AREA)
ori = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Original',ori)
cv2.imshow('SIFT',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# hog
img1 = cv2.imread(r'D:\computer_vision\data\tajmahal.jpg')
img = cv2.resize(img1,dim,interpolation=cv2.INTER_AREA)
ori = img.copy()
_, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, multichannel=True)
cv2.imshow('Original', ori)
cv2.imshow('HoG', hog_image)

# Feature Matching
import cv2
img1 = cv2.imread(r'D:\computer_vision\data\flower.jpeg', 0)
img2 = cv2.imread(r'D:\computer_vision\data\flower.jpeg', 0)
orb = cv2.ORB_create(nfeatures=500)
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
# It specifies the distance measurement to be used
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
# We sort them in ascending order of their distances so that best matches (with low distance) come to front
matches = sorted(matches, key=lambda x: x.distance)
match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)
cv2.imshow('original image', img1)
cv2.imshow('test image', img2)
cv2.imshow('Matches', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# translate the image x=25 pixels to the right and y=75 pixels up
translated = imutils.translate(img1, 25, -75)
# cv2.imshow('imutils_trans',translated)
# cv2.waitKey(0)

# skeleton = imutils.skeletonize(img1, size=(3, 3))
# cv2.imshow('skeleton',skeleton)
# cv2.waitKey(0)

resized = imutils.resize(img1, width=300)
cv2.imshow('imutils_trans',translated)
cv2.waitKey(0)


