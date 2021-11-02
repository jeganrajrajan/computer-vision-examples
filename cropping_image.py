import cv2

img = cv2.imread(r'D:\computer_vision\data\flower.jpeg')
y = 80
h = 150
x = 85
w = 180
new_cropped_img = img[y:y+h,x:x+w]
cv2.imshow('new_cropped',new_cropped_img)
cv2.waitKey(0)

# Start y: The starting y-coordinate. In this case, we start at y = 80.
# End y: The ending y-coordinate. We will end our crop at y = 80+150.
# Start x: The starting x-coordinate of the slice. We start the crop at x = 85.
# End x: The ending x-axis coordinate of the slice. Our slice ends at x = 85+180.