import cv2
import imutils
import matplotlib.pyplot as plt

# read image
image = cv2.imread(r'D:\computer_vision\data\flower.jpeg')
img_test = image.copy()
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(image,cv2.cv2.COLOR_BGR2GRAY)


# call imshow() using plt object
plt.axis('off')
plt.imshow(image)
# display that image
plt.show()

# change colour
# convert color image into grayscale image
img1 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# plot that grayscale image with Matplotlib
# cmap stands for colormap
plt.imshow(img1, cmap='gray')

# display that image
plt.show()


# vishuvalize without ticks
plt.imshow(img1)
# plt.imshow(img1,cmap='flag')
imgplot = plt.imshow(img)
imgplot.set_cmap('hot')
plt.imshow(img, cmap="hot")
plt.colorbar()
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

# multiple images plot


img = img1
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, th1 ,th2 ,th3 ,th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# img=cv2.imread('hanif.jpg')
# b,g,r=cv2.split(img)
# img_matplotlib=cv2.merge([r,g,b])


# INCORRECT: show the image without converting color spaces
plt.figure("Incorrect")
plt.imshow(img_test)
# CORRECT: convert color spaces before using plt.imshow
plt.figure("Correct")
plt.imshow(imutils.opencv2matplotlib(img3))
plt.show()


