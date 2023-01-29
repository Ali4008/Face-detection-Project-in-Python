import cv2
#LOADING THE CLASSIFIER
facescas=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#READING THE IMAGE
img=cv2.imread("people.jpeg")


#CONVERTING IMAGE TO GRAY SCALE
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Coodinates of a rectangle
faces=facescas.detectMultiScale(gray,1.2,5)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+h,y+w),(255,0,0),2)
    cv2.imshow("is",img)
    cv2.waitKey()
