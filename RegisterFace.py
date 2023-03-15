import os
import cv2

def RegisterFace():
    cam=cv2.VideoCapture(0)

    cur=os.getcwd()
    newdir=cur+"\\"+"photos"
    os.chdir(newdir)
    while True:
        _,frame=cam.read()
        cv2.imshow("Register Face  <Press q to capture>",frame)
        cv2.imwrite("img.png",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    os.chdir("..")