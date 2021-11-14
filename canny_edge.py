import cv2

# Read the original image
img = cv2.imread(r'D:\computer_vision\data\nemo.jpg',0)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img,(3,3),0)


# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)


# Sobel Edge Detection
# Read the original image
img1 = cv2.imread(r'D:\computer_vision\data\tiger.jpg',0)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img1,(3,3),0)
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection

# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)

cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)