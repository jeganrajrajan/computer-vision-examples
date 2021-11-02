import cv2
import numpy as np
image = cv2.imread(r"D:\computer_vision\data\flower.jpeg")
num_rows, num_cols = image.shape[:2]
translation_matrix = np.float32([ [1,0,70], [0,1,110] ])
img_translation = cv2.warpAffine(image, translation_matrix, (num_cols, num_rows), cv2.INTER_LINEAR)
cv2.imshow('img_transld',img_translation)
cv2.waitKey(0)
# changing value
translation_matrix = np.float32([ [1,0,-30], [0,1,-50] ])
img_translation = cv2.warpAffine(img_translation, translation_matrix, (num_cols + 70 + 30, num_rows + 110 + 50))
cv2.imshow('img_chng_translate',img_translation)
cv2.waitKey(0)

# rotation matrix
# rotation angle( here it is 30 degrees) with shrinkage of the image by 40%.
img_rotation = cv2.warpAffine(image, cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 0.6), (num_cols, num_rows))
cv2.imshow('img_rotation',img_rotation)
cv2.waitKey(0)
# getAffineTransformation function.

src_points = np.float32([[0,0], [num_cols-1,0], [0,num_rows-1]])
dst_points = np.float32([[0,0], [int(0.6*(num_cols-1)),0], [int(0.4*(num_cols-1)),num_rows-1]])
matrix = cv2.getAffineTransform(src_points, dst_points)
img_afftran = cv2.warpAffine(image, matrix, (num_cols,num_rows))
cv2.imshow('img_afftran',img_afftran)
cv2.waitKey(0)

# perpesctive transform
src_points = np.float32([[0,0], [num_cols-1,0], [0,num_rows-1], [num_cols-1,num_rows-1]])
dst_points = np.float32([[0,0], [num_cols-1,0], [int(0.33*num_cols),num_rows-1], [int(0.66*num_cols),num_rows-1]])
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_protran = cv2.warpPerspective(image, projective_matrix, (num_cols,num_rows))

cv2.imshow('img_perspective',img_protran)
cv2.waitKey(0)