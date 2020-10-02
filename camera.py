import cv2
import threading 

import imutils
from keras.models import load_model
import numpy as np

class VideoCamera(object):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    label_mapdisgust = ['enojado', 'neutral', 'miedo', 'feliz', 'triste', 'sorpresa', 'neutral']    
    model = load_model("/home/d/Documentos/flaskProject/Proyecto-Pyhton/modelo/model.h5")
    datos = [0,0,0,0,0,0,0]
       
    
    def __init__(self):
        # Open a camera
        self.cap = cv2.VideoCapture(0)      
    

    def __del__(self):
        print('elimina la grabacion')
        self.cap.release()
        

    def get_frame(self):
        padding = 20
        predicted_class=0
        ret, img = self.cap.read()
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x-padding, y-padding), (x+w+padding, y+h+padding), (255, 0, 0), 2)
                rostro = auxFrame[y-padding:y+h+padding,x-padding:x+w+padding]
                try:
                    rostro=imutils.resize(rostro, 48)
                except:
                    print("error transfomamcion")
                    continue
                
                if(not(rostro.shape[0]==48 and rostro.shape[1]==48)):
                    continue
                gray_small = rostro.reshape(1,48,48,1)               
                
                predicted_class = np.argmax(self.model.predict(gray_small))
                self.datos[predicted_class]= self.datos[predicted_class]+1
                
                cv2.putText(img,'{}'.format(self.label_mapdisgust[predicted_class]),(x,y-25),2,1.1,(0,0,255),1,cv2.LINE_AA)                
            
            ret, jpeg = cv2.imencode('.jpg', img)
            return jpeg.tobytes()      
        else:
            # self.__del__()        
            return None



            