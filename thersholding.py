import cv2

img = cv2.imread(r'D:\computer_vision\data\excel-invoice-template.png',0)

# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
# ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
# ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
# ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
# ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
# ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
#
# # the window showing output images
# # with the corresponding thresholding
# # techniques applied to the input images
# cv2.imshow('Binary Threshold', thresh1)
# cv2.imshow('Binary Threshold Inverted', thresh2)
# cv2.imshow('Truncated Threshold', thresh3)
# cv2.imshow('Set to 0', thresh4)
# cv2.imshow('Set to 0 Inverted', thresh5)
#
# # De-allocate any associated memory usage
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()

# otsu thersholding
(T, threshInv) = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

#adaptive thersholding
image = cv2.imread(r'D:\computer_vision\data\bookpage.jpg')
gray_scale_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
th = cv2.adaptiveThreshold(gray_scale_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()