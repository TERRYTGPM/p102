import cv2

def useCamera():
     videocaptureobject = cv2.VideoCapture(0)
     isCameraOn = True

     while(isCameraOn):

          ret, frame = videocaptureobject.read()
          cv2.imwrite("lllll1llll.png", frame)

          isCameraOn = False

     videocaptureobject.release()

     cv2.destroyAllWindows()

useCamera()