import time
import sys
import numpy as np
import cv2
import cv2.aruco as aruco
import numpy as np
import math


# reading calibration matrices
calib_path  = ""

mtx   = np.loadtxt(calib_path+'cameraMatrix.txt', delimiter=',')
distor   = np.loadtxt(calib_path+'cameraDistortion.txt', delimiter=',')

print("--------------------")
print(mtx)
print("--------------------")
print(distor)
print("--------------------")

aruco_dict  = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

#--- Capture the videocamera (this may also be a video or a picture)
cap = cv2.VideoCapture(0)
#-- Set the camera size as the one it was calibrated with
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#-- Font for the text in the image
font = cv2.FONT_HERSHEY_PLAIN

tvec0 = np.array([[[0.0, 0.0, 0.0]]])
rvecmax = 0.0

while True:
    #-- Read the camera frame
    ret, frame = cap.read()
    #-- Convert in gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #-- remember, OpenCV stores color images in Blue, Green, Red

    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict) # camera_matrix, camera_distortion?
    
    image = aruco.drawDetectedMarkers(gray, corners)

    rvec, tvec ,_ = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, distor)

    if ids is not None:
        for i in range(0, ids.size):
            aruco.drawAxis(image, mtx, distor, rvec[0], tvec[0], 0.06) # np.array([0.0, 0.0, 0.0])
            cv2.putText(image, "%.1f cm -- %.0f deg" % ((tvec[0][0][2] * 100), (rvec[0][0][2] / math.pi * 180)), (0, 230), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (244, 244, 244))
            R, _ = cv2.Rodrigues(rvec[0]) # ?
            cameraPose = -R.T * tvec[0] # ?
            """
            if ((rvec[0][0][1])) > rvecmax:
                rvecmax = (rvec[0][0][1]);
            print((int)(rvec[0][0][0] / math.pi * 180), " ", (int)(rvec[0][0][1] / math.pi * 180), " ", (int)(rvec[0][0][2] / math.pi * 180))
            #print(rvec.shape)
            """

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

