#importacion de modulos
import cv2
import numpy as np

#Carga la imagen
imagen1 = cv2.imread("original.jpg",0)
imagen11 = cv2.imread("original.jpg",1)
for imagen in range(1,5,1):
    IMAGEN=str(imagen)
    template_color = cv2.imread(IMAGEN + '.jpg', 1)
    # para mostrar la imgen
    print("La forma de la imagen original es: ", imagen1.shape)
    print("La forma de la imagen plantilla es: ", template_color.shape)
    cv2.imshow(IMAGEN+'numero', template_color)
    # Definimos imagen ROI
    template = cv2.cvtColor(template_color, cv2.COLOR_BGR2GRAY)
    template_layers = template_color.copy()
    # A cada capa le asigno blanco y negro
    template_layers[:, :, 0] = template  # Capa B
    template_layers[:, :, 1] = template  # Capa G
    template_layers[:, :, 2] = template  # Capa R
    umbral = 99999
    for x in range(0, 6):
        for y in range(0, 4):
            ROI = imagen1[y*100:100*(y+1),x*100:100*(x+1)]
            diferencia = cv2.absdiff(template, ROI)
            Sum = np.sum(diferencia)
            print(Sum)
            if Sum < umbral:
                umbral = Sum
                print(Sum)
            if Sum <= umbral:
                cv2.imshow('Resta', diferencia)
                imagen11[y*100:100*(y+1),x*100:100*(x+1)] = template_layers
                cv2.rectangle(imagen11, (x*100, y*100), ((x+1)*100,(y+1)*100), (0, 0, 255), 3)
                cv2.imshow("hola", imagen1)
                cv2.imshow('resultado', ROI)
                cv2.imshow(IMAGEN+' Resultados', imagen11)

cv2.waitKey(0)
#Acceder al valor de pixel en las coordenadas (x,y)=(50,100)