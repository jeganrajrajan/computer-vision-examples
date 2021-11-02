import numpy as np
import cv2

# Creating a black image with 3 channels
# RGB and unsigned int datatype
create_img = np.zeros((500, 500, 3), dtype="uint8")
# cv2.imshow('dark', create_img)
#
# # Allows us to see image
# # until closed forcefully
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # draw line
# line_img = cv2.line(create_img, (100,100), (300,300), (0,255,0),4)
# cv2.imshow('line', line_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# draw rectangle
# rect_img = cv2.rectangle(create_img, (250,30), (450,200), (0,0,255), 5)
# cv2.imshow('rect', rect_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # filled_rect
# fill_rect_img = cv2.rectangle(create_img, (250,30), (450,200), (0,255,0), -1)
# cv2.imshow('fill_rect_img ', rect_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# draw circle
# circle_img = cv2.circle(create_img, (200, 200), 80, (255, 0, 0), -1)
# cv2.imshow('circle', circle_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ellipse
ellipse_img = cv2.ellipse(create_img, (300, 450), (100, 50), 45, 130, 270, (255,255,255), 1)
cv2.imshow('ellipse', ellipse_img)
cv2.waitKey(0)
cv2.destroyAllWindows()