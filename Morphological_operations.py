import cv2
import os 


#First we will perform morphological operation to remove noise and hair.
cancerNames = list()
cancerNames = ["MEL", "NV", "AKIEC", "BCC", "BKL", "DF", "VASC"]

for i in cancerNames:
    path = 'F:\\Skin_Cancer\\Final\\Class\\'+i
    images = os.listdir(path)
    for image in images:
        img = cv2.imread('F:\\Skin_Cancer\\Final\\Class\\'+i+'\\'+image)
        kernel = np.ones((5,5), np.uint8)
        img_erosion = cv2.erode(img, kernel, iterations=1)
        img_dilation = cv2.dilate(img, kernel, iterations=2)
        cv2.imwrite('F:\\Skin_Cancer\\Final\\Class\\'+i+'\\'+image, img_dilation)