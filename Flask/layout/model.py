from mtcnn import MTCNN
import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

def crop_image(image_path):
    detector = MTCNN() 
    img=cv2.imread(image_path)
    data=detector.detect_faces(img)
    biggest=0
    if data !=[]:
        for faces in data:
            box=faces['box']            
            # calculate the area in the image
            area = box[3]  * box[2]
            if area>biggest:
                biggest=area
                bbox=box 
        bbox[0]= 0 if bbox[0]<0 else bbox[0]
        bbox[1]= 0 if bbox[1]<0 else bbox[1]
        img=img[bbox[1]: bbox[1]+bbox[3],bbox[0]: bbox[0]+ bbox[2]] 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert from bgr to rgb
        zoom1 = cv2.resize(img, (112, 112), interpolation=cv2.INTER_CUBIC)
        return (True, zoom1) 
    else:
        return (False, None)