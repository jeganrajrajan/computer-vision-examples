import cv2

img = cv2.imread(r"D:\computer_vision\data\flower.jpeg")
run =False
def draw_circle(event, x, y, flags, param):
    global run
    if event == cv2.EVENT_LBUTTONDOWN:
        run=True
        cv2.circle(img, (x, y), 20, (0, 255, 0), -1)
    if event == cv2.EVENT_LBUTTONUP:
        run = False
    if event == cv2.EVENT_MOUSEMOVE:
        if run==True:
            cv2.circle(img, (x, y), 20, (255, 0, 0), -1)
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", draw_circle)

while True:
    cv2.imshow("Window", img)
    k = cv2.waitKey(1)
    if k == ord('c'):
        img = cv2.imread(r"D:\computer_vision\data\flower.jpeg")
    if k == 27:
        cv2.destroyAllWindows()
        break







# import cv2
#
# img = cv2.imread(r"D:\computer_vision\data\flower.jpeg")
# run = False
#
# def draw_circle(event, x, y,flags, param):
#     global run
#     if event == cv2.EVENT_LBUTTONDOWN:
#         run = True
#         print("hello")
#         cv2.circle(img, (x, y), 20, (0, 255, 0), -1)
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if run == True:
#             cv2.circle(img, (x, y), 20, (0, 255, 0), -1)
#
#
#
# cv2.namedWindow(winname="Window")
# cv2.setMouseCallback("Window", draw_circle)
#
# while True:
#     cv2.imshow("Window", img)
#     k = cv2.waitKey(1)
#     if k == ord('c'):
#         img = cv2.imread(r"D:\computer_vision\data\flower.jpeg")
#     if k == 27:
#         cv2.destroyAllWindows()
#         break
# cv2.destroyAllWindows()
