import cv2
import imutils

# load the haar cascade face detector from
print("[INFO] loading face detector...")
detector = cv2.CascadeClassifier(r"D:\computer_vision\data\haarcascades\haarcascade_frontalface_alt.xml")
# load the input image from disk, resize it, and convert it to
# grayscale
image = cv2.imread(r"D:\computer_vision\data\multiple_face.jpeg")
image = imutils.resize(image, width = 500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the input image using the haar cascade face
# detector
print("[INFO] performing face detection...")
rects = detector.detectMultiScale(gray, scaleFactor = 1.05,
                                  minNeighbors = 7, minSize = (30, 30),
                                  flags = cv2.CASCADE_SCALE_IMAGE)
print("[INFO] {} faces detected...".format(len(rects)))
# loop over the bounding boxes
for (x, y, w, h) in rects:
    x = x-10
    y = y-20
    # draw the face bounding box on the image
    cv2.rectangle(image, (x, y), (x + w+15, y + h+30), (0, 255, 0), 2)
# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)



# video file
face_cascade = cv2.CascadeClassifier(r'D:\computer_vision\data\haarcascades\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier(r'D:\computer_vision\data\haarcascades\haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(r'D:\computer_vision\data\haarcascades\haarcascade_smile.xml')
cap = cv2.VideoCapture(r'D:\computer_vision\data\171124_C1_HD_002.mp4')

while 1:
    ret, image = cap.read()
    img = imutils.resize(image, width = 500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        smile = smile_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 255), 2)

        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()

