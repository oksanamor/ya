import cv2
import numpy as np
import math

def theta(x1,y1,x2,y2):
    t=math.atan2(x2-x1,y2-y1)
    t=t*180/math.pi+90 #Смещение угла на 90 градусов для удобства расчетов
    print(t)
    print(x1,y1,x2,y2)
    return t

cap=cv2.VideoCapture("video_2018-03-18_22-00-36.mp4")
while True:
    ok, image = cap.read()
    if not ok:
        break


    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    im_blur=cv2.GaussianBlur(im_gray,(9,9),200)
    im_canny=cv2.Canny(im_gray, 100, 400)
    cv2.imshow("Canny",im_canny)
    #-----------------------------------------------------
    lines = cv2.HoughLinesP(im_canny, 1, np.pi / 180, 50, np.array([]), minLineLength=50, maxLineGap=50)
    try:
        a, b, c = lines.shape
    except AttributeError:
        a = 0
    for i in range(a):
        x1,y1,x2,y2=lines[i][0][0], lines[i][0][1],lines[i][0][2], lines[i][0][3]
        t=theta(x1,y1,x2,y2)

        if (240<t<260 or 50<t<70): #Левая линия разметки
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 255), 7, cv2.LINE_AA) #Желтый
        if (220<t<240 or 30<t<50):
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 7, cv2.LINE_AA) #Синий
        if (250<t<270 or 70<t<90):
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 7, cv2.LINE_AA) #Красный
        if (90<t<110 or 270<t<290): #Правая линия разметки
            cv2.line(image, (x1,y1),(x2,y2), (0, 255, 0),7,cv2.LINE_AA) #Зеленый
        if (110<t<135 or 290<t<315):
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 125), 7, cv2.LINE_AA) #Оранжевый
        if (135<t<160 or 315<t<340):
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 7, cv2.LINE_AA) #Фиолетовый
        if (0<t<5 or 175<t<185):
            cv2.line(image, (x1, y1), (x2, y2), (255, 255, 255), 7, cv2.LINE_AA) #Stop_line
            print("Stop")


    window_name = "Stream"
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    cv2.imshow(window_name,image)
    if cv2.waitKey(30)>0:
        break

