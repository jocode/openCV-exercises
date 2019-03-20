# -*- coding: utf-8 -*-
import cv2 
import numpy as np 

# Recibo el nombre de la plantilla
imagen = str(raw_input('Ingrese el nombre de la imagen plantilla (.jpg): '))

#Leer la imagen principal 
img_rgb = cv2.imread('original.jpg')
cv2.imshow('Original',img_rgb) 

#Convertir a escala gris 
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow('Escala de grises',img_rgb) 

#Leer la plantilla 
template = cv2.imread(imagen+'.jpg', 0)

# Almacenar la anchura (w) y la altura (h) de la plantilla
w, h = template.shape[::-1] 
 
# Realizar operaciones de coincidencia
res = cv2.matchTemplate(img_gray, template,cv2.TM_CCOEFF_NORMED)
 
#Especificar un umbral (threshold)
threshold = 0.8
 
# Almacenar las coordenadas del área coincidente en un array numpy
loc = np.where( res >= threshold) 
 
#Dibujar un rectángulo alrededor de la región adaptada encontrada
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
 
#Mostrar la imagen final con el área correspondiente
cv2.imshow('eye',template)
cv2.imshow('Detectado',img_rgb)
cv2.waitKey(0)