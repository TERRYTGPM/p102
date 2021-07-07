import dropbox
import time
import random
import cv2

startTime = time.time()

def takeSnapshot():
    number = str(random.randint(1, 500000))
    videocaptureobject = cv2.VideoCapture(0)

    true = True

    while(true == True):
        ret, frame = videocaptureobject.read()

        imageName = "img"+number+".png"

        cv2.imwrite(imageName, frame)

        startTime = time.time()

        true = False

    return imageName

    print(imageName+"AYYYYYYYYYYYYYYYYYYYYYYYYYYAYAY")

    videocaptureobject.release()

    cv2.destroyAllWindows()

def uploadFile(imagename):
    number = str(random.randint(1, 500000))
    acessToken = "Rhio0svSNHAAAAAAAAAAAcD4onoXed70XQG6E5pl53MtlxEGHDcfEc2bob7c06km"

    car = "image"+number+".png"

    filefrom,fileto = imagename, "/photos/"+car

    dbx = dropbox.Dropbox(acessToken)

    with open(filefrom, 'rb') as l:
        dbx.files_upload(l.read(), fileto, mode=dropbox.files.WriteMode.overwrite)

    print("file uploaded")

def runFunctions():
    while True:
        if((time.time()-startTime)>=500):
            var = takeSnapshot()
            uploadFile(var)

runFunctions()