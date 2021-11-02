import PIL
from PIL import Image
import cv2

# Location of the image
img = Image.open(r"D:\computer_vision\data\hat_ex.png")

img.show()

# size of the image
print(img.size)

# format of the image
print(img.format)
# mode of the image
print(img.mode)

img1 = img.rotate(90, PIL.Image.NEAREST, expand = 1)
img1.show()

# Flipping the Image
img2 = Image.open(r'D:\computer_vision\data\A._P._J._Abdul_Kalam.jpg')
vertical_img = img2.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save("vertical.png")

vertical_img.show()

# Resizing the image
width, height = img2.size

# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5

# Cropped image of above dimension
# (It will not change original image)
im1 = img2.crop((left, top, right, bottom))
newsize = (300, 300)
im1 = im1.resize(newsize)

# Saving the Image
im1.save('test_resized_img.png')
# Merging Images

# Splitting the image into individual
# bands
img_colr = Image.open(r'D:\computer_vision\data\apple_image.jpg')
r, g, b, = img_colr.split()

# merge function used
im1 = Image.merge('RGB', (g, b, r))
im1.show()

import numpy as np
img = cv2.imread(r"D:\computer_vision\data\bookpage.jpg")

# You may need to convert the color.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
im_pil = Image.fromarray(img)

# For reversing the operation:
im_np = np.asarray(im_pil)