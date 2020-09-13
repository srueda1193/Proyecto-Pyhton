import cv2
import imutils
from keras.models import load_model
import numpy as np

import sqlite3

connectionObject = sqlite3.connect("templates/database/proyecto_python.db")
cursorObject = connectionObject.cursor()
# createTable = "CREATE TABLE EMP(id int,idPersona varchar(10), idSecion int, enojado, disgusto, miedo, feliz, triste, sorpresa, neutral)"

# cursorObject.execute(createTable)



import time
# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

label_mapdisgust = ['enojado', 'disgusto', 'miedo', 'feliz', 'triste', 'sorpresa', 'neutral']


model = load_model("/home/d/Descargas/model_filter.h5")

datos = [0,0,0,0,0,0,0]
contador=0
secion = "4"
# To capture video from webcam. 
cap = cv2.VideoCapture(0)
padding = 20

persona = "1717171717"
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
predicted_class=0
while True:
    # Read the frame
    # time.sleep(1)
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # gray_small = imutils.resize(gray, 48)
    

    auxFrame = gray.copy()
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x-padding, y-padding), (x+w+padding, y+h+padding), (255, 0, 0), 2)
        rostro = auxFrame[y-padding:y+h+padding,x-padding:x+w+padding]
        try:
            rostro=imutils.resize(rostro, 48)
        except:
            print("error transfomamcion")
            continue
        # print(rostro.shape)
        if(not(rostro.shape[0]==48 and rostro.shape[1]==48)):
            continue# model = load_model("/home/d/Descargas/Fer2013_55E.hdf5")#1
        gray_small = rostro.reshape(1,48,48,1)
        
        # rostro = cv2.resize(rostro,(50,50),interpolation= cv2.INTER_CUBIC)
        predicted_class = np.argmax(model.predict(gray_small))
        datos[predicted_class]= datos[predicted_class]+1
        # predicted_class = model.predict(gray_small)
        cv2.putText(img,'{}'.format(label_mapdisgust[predicted_class]),(x,y-25),2,1.1,(0,0,255),1,cv2.LINE_AA)
        # print(label_mapdisgust[predicted_class])
    # Display
    if(sum(datos)>=10):
        # print(contador,datos)
        normalizados = [float(i)/sum(datos) for i in datos]
        insertValues = "INSERT INTO DATA values("+str(contador)+","+persona+","+secion+","+str(normalizados[0])+","+str(normalizados[1])+","+str(normalizados[2])+","+str(normalizados[3])+","+str(normalizados[4])+","+str(normalizados[5])+","+str(normalizados[6])+")"
        cursorObject.execute(insertValues)
        # print(normalizados)
        contador = contador + 1
        datos = [0,0,0,0,0,0,0]
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        connectionObject.commit()
        queryTable = "SELECT * from DATA where idSecion = "+secion
        queryResults = cursorObject.execute(queryTable)
        print("Datos registrados:",persona)

        for result in queryResults:
            print(result)

        connectionObject.close()
        break
# Release the VideoCapture object
cap.release()