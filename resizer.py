
import numpy as np
import cv2
import os

dir_path = 'D:\\RahulDhar\\Client_Gurbage_Detection\\image'
path = 'D:\\RahulDhar\\Client_Gurbage_Detection\\dataset'

for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith((".JPG", ".jpg")):
        image = cv2.imread(os.path.join(dir_path, filename))
        resized = cv2.resize(image,(416, 231), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(path , filename),resized)
