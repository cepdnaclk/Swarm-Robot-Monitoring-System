import cv2
import numpy as np

cX =[0,0,0,0,0]
cY =[0,0,0,0,0]
cX1=[1,1,1,1,1]
cX2=[0,0,0,0,0]
cY1=[1,1,1,1,1]
cY2=[0,0,0,0,0]


cap = cv2.VideoCapture("Message.mp4")
#take the camera video

ret,frame1 = cap.read()
ret,frame2 = cap.read()

num=["Rob1","Rob2","Rob3","Rob4","Rob5"]
#Initialise robot name array
i=0
j=0
r=0
y=0
while cap.isOpened():
    ret,frame1 = cap.read()
    hsv1 =cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    hsv2=cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([39,145,7])
    upper_blue = np.array([127,185,224])
    mask1 =cv2.inRange(hsv1,lower_blue,upper_blue)
    mask2 =cv2.inRange(hsv2,lower_blue,upper_blue)
    contours,_ = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #blue color Contours identify
    
    
    
    lower_red = np.array([39,221,0])
    upper_red = np.array([255,255,255])
    mask_red =cv2.inRange(hsv1,lower_red,upper_red)
    
    #only red color identify contour
    
    

    
    lower_yellow = np.array([6,69,39])
    upper_yellow = np.array([53,255,255])
    mask_yel =cv2.inRange(hsv1,lower_yellow,upper_yellow)
    
    #only yellow color identify contour
    
    
    contours_yellow,_ = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        M=cv2.moments(contour)
        x=int(M["m10"] / M["m00"])
        y=int(M["m01"] / M["m00"])
        
        contours_red,_ = cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
         for conred in contours_red:#identify red contours center
             
        
             M1=cv2.moments(con_red)
             x_red=int(M1["m10"] / M1["m00"])
             y_red=int(M1["m01"] / M1["m00"]
                 if x==x_red:
                   print(num[i])
                   print(" Red Message")
                      r=i
          
        for con_yel in contours_yel:
        
               M2=cv2.moments(con_yel)
               x_yel=int(M2["m10"] / M2["m00"])
               y_yel=int(M["m01"] / M["m00"]
               if x==x_yel:
                 print(num[i])
                 print(" Yellow Message")
                 y=i
                     
            
        
        if cX2[0]<cX[0]<cX1[0]  & cY2[0]<cY[0]<cY1[0]:
                j=0
        elif cX2[1]<cX[1]<cX1[1]  & cY2[1]<cY[1]<cY1[1]:
                j=1
        elif cX2[2]<cX[2]<cX1[2]  & cY2[2]<cY[2]<cY1[2]:
                j=2
        elif cX2[3]<cX[3]<cX1[3]  & cY2[3]<cY[3]<cY1[3]:
                j=3
        elif cX2[4]<cX[4]<cX1[4]  & cY2[4]<cY[4]<cY1[4]:
                j=4
         
        
        cX[i] = x
        cY[i] = y

        cX1[i]=x+5
        cX2[i]=x-5

        cY1[i]=y+5
        cY2[i]=y-5
        
        if 1<cv2.contourArea(contour)<3:
            #continue
           cv2.drawContours(frame1, [contour], -1, (0, 255, 0), 2)
           cv2.circle(frame1, (x, y), 7, (0, 255, 20), -1)
           cv2.putText(frame1,num[j], (x - 20, y - 20),
		   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
           if i<5:
            i=i+1
        
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    cv2.imshow("inter",frame1)
    
    
    frame1=frame2
    ret,frame2 = cap.read()
    i=0
    j=0
    if cv2.waitKey(40)==27:
        break
    
cv2.destroyAllWindows()
cap.release()
    
    
    
    
