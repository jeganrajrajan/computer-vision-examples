import cv2
import dlib
import imutils
import numpy as np

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r'D:\computer_vision\data\haarcascades\shape_predictor_68_face_landmarks.dat')
cap = cv2.VideoCapture(r'D:\computer_vision\data\171124_C1_HD_002.mp4')

while True:
    # Capture the image from the webcam
    ret, img = cap.read()
    image = imutils.resize(img, width = 500)
    # Convert the image color to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect the face
    rects = detector(gray, 1)
    # Detect landmarks for each face
    for rect in rects:
        # Get the landmark points
        shape = predictor(gray, rect)
        # Convert it to the NumPy Array
        shape_np = np.zeros((68, 2), dtype = "int")
        for i in range(0, 68):
            shape_np[i] = (shape.part(i).x, shape.part(i).y)
        shape = shape_np

        # Display the landmarks
        for i, (x, y) in enumerate(shape):
            # Draw the circle to mark the keypoint
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
            # Display the image
    cv2.imshow('Landmark Detection', image)

    # Press the escape button to terminate the code
    if cv2.waitKey(10) == 27:
        break

cap.release()



# from image
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r'D:\computer_vision\data\haarcascades\shape_predictor_68_face_landmarks.dat')

img = cv2.imread(r"D:\computer_vision\data\multiple_face.jpeg")
image = imutils.resize(img, width = 500)
# Convert the image color to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect the face
rects = detector(gray, 1)
# Detect landmarks for each face
for rect in rects:
    # Get the landmark points
    shape = predictor(gray, rect)
    # Convert it to the NumPy Array
    shape_np = np.zeros((68, 2), dtype = "int")
    for i in range(0, 68):
        shape_np[i] = (shape.part(i).x, shape.part(i).y)
    shape = shape_np

    # Display the landmarks
    for i, (x, y) in enumerate(shape):
        # Draw the circle to mark the keypoint
        cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
        # Display the image
cv2.imshow('Landmark Detection', image)
cv2.waitKey(0)


