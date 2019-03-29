# -*- coding: utf-8 -*-
import cv2 
import numpy as np

# Leo la imágen tal cual, con los 4 canales (El último es el canal alfa) puede leerse como cv2.IMREAD_UNCHANGED ó -1
fondo = cv2.imread('fondo.jpg')
fondo = cv2.resize(fondo, (500, 500))
logo = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (500, 500))
print('Primer plano ', logo.shape)

# Extraigo el canal alfa de la imagen, ésta sera nuestra máscara
canal_alfa = logo[:,:,3]

# Obtengo la imagen de la imagen a sobreponer sólo los 3 canales
logo_3_canales = logo[:,:,0:3]

# Defino el canal alfa con 3 canales
canal_alfa = cv2.merge((canal_alfa, canal_alfa, canal_alfa))

""" Proceso de Fusión """
# Convertimos las imágenes, en imágenes de punto flotante
logo_3_canales = logo_3_canales.astype(float)
fondo = fondo.astype(float)

# Normalizar máscara Alfa para mantener intensidad entre 0 y 1
canal_alfa = canal_alfa.astype(float)/255.0

# Multiplicacion canal alfa y primer plano
logo_3_canales = cv2.multiply(canal_alfa, logo_3_canales)

# Multiplicacion fondo con (1 - canal alfa)
fondo = cv2.multiply( (1.0 - canal_alfa), fondo)

# Adición de logo_3_canales y fondo
resultado = cv2.add(logo_3_canales, fondo)


cv2.imshow('Canal Alfa', (resultado/255) )
cv2.waitKey(0)
cv2.destroyAllWindows()