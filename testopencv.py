import cv2
import numpy as np

lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])

lower_yellow = np.array([22,93,0])
upper_yellow = np.array([45,255,255])

cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
    contor,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contor:
        area=cv2.contourArea(c)
        if area >300:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.drawContours(frame,c,-1,(0,255,0))

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    if cv2.waitKey(10)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

