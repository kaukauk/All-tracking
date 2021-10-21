import cv2
from all_tracking_utils import detector

# Choose one out of 'hands, pose, face_mesh'
detect = detector('face_mesh')

cap = cv2.VideoCapture(1) # Check for error

while True:
    success, img = cap.read()

    img, lm_list = detect.find_lms(img, draw=False)

    detect.display_img(img)
