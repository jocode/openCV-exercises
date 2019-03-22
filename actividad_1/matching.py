# -*- coding: utf-8 -*-
import cv2 
import numpy as np 

# Recibo el nombre de la plantilla
imagen = str(raw_input('Ingrese el nombre de la imagen plantilla (.jpg): '))

#Leer la imagen principal 
img_color = cv2.imread('original.jpg')
cv2.imshow('Original',img_color) 

#Convertir a escala gris 
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('Escala de grises',img_color) 

#Leer la plantilla 
template_color = cv2.imread(imagen+'.jpg', 1)
template = cv2.cvtColor(template_color, cv2.COLOR_BGR2GRAY)

# Defino una nueva imagen de 3 canales a blanco y negro para el la región de coincidencia
template_layers = template_color.copy()
# A cada capa le asigno blanco y negro
template_layers[:,:,0] = template # Capa B
template_layers[:,:,1] = template # Capa G 
template_layers[:,:,2] = template # Capa R


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
	# El punto (pt) es (y, x)   =>  y = filas, x = columnas
	img_color[pt[1]:pt[1]+h, pt[0]:pt[0]+h] = template_layers
	cv2.rectangle(img_color, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
 
#Mostrar la imagen final con el área correspondiente
cv2.imshow('Objeto',template)
cv2.imshow('Detectado',img_color)
cv2.waitKey(0)