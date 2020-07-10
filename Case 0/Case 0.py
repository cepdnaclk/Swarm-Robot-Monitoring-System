import cv2
import numpy as np


cap = cv2.VideoCapture("Message.mp4")


ret,frame2 = cap.read()

num=["Rob1","Rob2","Rob3","Rob4","Rob5"]
i=0
while cap.isOpened():
    ret,frame1 = cap.read()
    hsv1 =cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    #hsv2=cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([39,145,7])
    upper_blue = np.array([127,185,224])
    mask1 =cv2.inRange(hsv1,lower_blue,upper_blue)
    #mask2 =cv2.inRange(hsv2,lower_blue,upper_blue)
    #kernal = np.ones((5,5),np.float32)/25
    #mask3 = cv2.GaussianBlur(mask1,(5,5),1)
    
    contours,_ = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        
        if cv2.contourArea(contour)<700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1, num[i], (x - 20, y - 20),
		   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        if i<5:
         i=i+1
        
    cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    cv2.imshow("inter",frame1)
    
    
    
    ret,frame2 = cap.read()
    frame1=frame2
    i=0
    if cv2.waitKey(40)==27:
        break
    
cv2.destroyAllWindows()
cap.release()
    
    
    
  
        

    
    
