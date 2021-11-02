import cv2
from matplotlib import pyplot as plt

image = cv2.imread(r"D:\computer_vision\data\flower.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# compute a grayscale histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# matplotlib expects RGB images so convert and then display the image
# with matplotlib
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
# plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])


# normalize the histogram
hist /= hist.sum()
# plot the normalized histogram
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("% of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# histogram equalization
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(image)
cv2.imshow("Input", image)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)

# adaptive
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equalized = clahe.apply(image)
cv2.imshow("Input", image)
cv2.imshow("adptive Histogram Equalization", equalized)
cv2.waitKey(0)
