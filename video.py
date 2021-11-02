import numpy as np
import cv2
import requests
import imutils

# # cap = cv2.VideoCapture(0)
# #
# # while (True):
# #     ret, frame = cap.read()
# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #
# #     cv2.imshow('frame', gray)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # cap.release()
# # cv2.destroyAllWindows()
#
#
# # Recording
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#
# while (True):
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     out.write(frame)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# Import essential librarieqs

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://192.168.2.102:8080/shot.jpg"

# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("Android_cam", img)

    # Press Esc key to exitq
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()


# open videos accessing frames
# Create a VideoCapture object and read from input file
# cap = cv2.VideoCapture(r'D:\computer_vision\data\sample_video.mp4')
#
# # Check if camera opened successfully
# if (cap.isOpened() == False):
#     print("Error opening video file")
#
# # Read until video is completed
# while (cap.isOpened()):
#
#         # Capture frame-by-frame
#         ret, frame = cap.read()
#         if ret == True:
#             # Display the resulting frame
#             cv2.imshow('Frame', frame)
#
#             # Press Q on keyboard to exit
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                 break
#
#         # Break the loop
#         else:
#             break
# When everything done, release
# the video capture object
# cap.release()
#
# # Closes all the frames
# cv2.destroyAllWindows()
#
# # accessing the frames
# cap = cv2.VideoCapture(r'D:\computer_vision\data\sample_video.mp4')
# i = 0
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == False:
#         break
#     cv2.imwrite(r'D:\computer_vision\data\output/frame' + str(i) + '.png', frame)
#     i += 1
# total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# fps = cap.get(cv2.CAP_PROP_FPS)
# print(total)
# # cap.release()
# # cv2.destroyAllWindows()