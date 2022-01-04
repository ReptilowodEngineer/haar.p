import cv2
import time
bag_cascade=cv2.CascadeClassifier('C:/Users/messi/Desktop/OpenCV_automobile/Bags/ha/cascade.xml')
img = cv2.imread('C:/Users/messi/Desktop/OpenCV_automobile/Bags/Good/7.jpg')
z=1.5
def v():
    z=1.5
    time.sleep(0.1)
    z = 1.8
    time.sleep(0.1)
    z = 2
    time.sleep(0.1)

v()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bag = bag_cascade.detectMultiScale(gray, z, 5)

for (x, y, w, h) in bag:


    org=(x, y-20)
    cv2.putText(img, 'Bag', org, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 1)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]



                        # When everything is done, release the capture






cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
