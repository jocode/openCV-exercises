# -*- coding: utf-8 -*-
import cv2 
import numpy as np

# Defino el tamaño que tendrá el ícono
size_icon = 100

# Leo la imágen tal cual, con los 4 canales (El último es el canal alfa) puede leerse como cv2.IMREAD_UNCHANGED ó -1
fondo = cv2.imread('fondo.jpg')
fondo = cv2.resize(fondo, (1000, 500))
logo = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (size_icon, size_icon))
h, w, _ = fondo.shape
print('Tamaño, ', w, h)
print('Primer plano ', logo.shape)

# Extraigo el canal alfa de la imagen, ésta sera nuestra máscara
canal_alfa = logo[:,:,3]

# Obtengo la imagen de la imagen a sobreponer sólo los 3 canales
logo_3_canales = logo[:,:,0:3]

# Defino el canal alfa con 3 canales
canal_alfa = cv2.merge((canal_alfa, canal_alfa, canal_alfa))

# Defino la Región donde colocaré el logo (ROI)
ROI = fondo[ (h-size_icon):h, (w-size_icon):w]

""" Proceso de Fusión """

# Convertimos las imágenes, en imágenes de punto flotante
logo_3_canales = logo_3_canales.astype(float)
ROI = ROI.astype(float)

# Normalizar máscara Alfa para mantener intensidad entre 0 y 1
canal_alfa = canal_alfa.astype(float)/255.0

# Multiplicacion canal alfa y primer plano
logo_3_canales = cv2.multiply(canal_alfa, logo_3_canales)

# Multiplicacion fondo con (1 - canal alfa)
ROI = cv2.multiply( (1.0 - canal_alfa), ROI)

# Adición de logo_3_canales y fondo
resultado = cv2.add(logo_3_canales, ROI)

# Agrego la región a la imagen final
fondo[ (h-size_icon):h, (w-size_icon):w] = (resultado)


cv2.imshow('Canal Alfa',  fondo)
cv2.waitKey(0)
cv2.destroyAllWindows()