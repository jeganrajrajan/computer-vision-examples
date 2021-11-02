import numpy as np
import cv2

img = np.zeros((600, 600, 3), dtype = "uint8")

# penta = np.array([[[40,160],[120,100],[200,160],[160,240],[80,240]]], np.int32)
# triangle = np.array([[[240, 130], [380, 230], [190, 280]]], np.int32)
# cv2.polylines(img, [triangle], False, (0,255,0), thickness=3)
#
# img_mod = cv2.polylines(img, [penta], True, (255,120,255),3)
#
# cv2.imshow('Shapes', img_mod)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# puttext
image = cv2.putText(img, 'triangle&polygon', (50,50), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (255, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('puttext', image)

cv2.waitKey(0)
cv2.destroyAllWindows()