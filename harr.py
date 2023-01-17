# Importing OpenCV package
import cv2
import os

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path = "lfw-deepfunneled/"
dir_list = os.listdir(path)

num_dir = 0
for dir in dir_list:
    if dir == ".DS_Store":
        continue
    file_list = os.listdir(path+dir)
    z=0
    for file in file_list:
        # Reading the image
        img = cv2.imread(path+dir+"/"+file)
          
        # Converting image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
          
        # Applying the face detection method on the grayscale image
        faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)
          
        # Iterating through rectangles of detected faces
        i = 0
        for (x, y, w, h) in faces_rect:
            crop_img = img[y:y+h, x:x+w]
            file_name = "lfw-deepfunneled-ad/"+dir+"/"+str(z)+"_"+str(i)+".jpg"
            print(w,h)
            cv2.imwrite(file_name, crop_img)
            i+=1
        z+=1
    num_dir+=1
  
