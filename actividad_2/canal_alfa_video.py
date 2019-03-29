# -*- coding: utf-8 -*-
import cv2
import numpy as np 

""" Declaracion de variables """
# Defino el tamaño del ícono
SIZE_ICON = 100
logo = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (SIZE_ICON, SIZE_ICON))
# Tomo el canal alfa
canal_alfa = logo[:,:,3]
# Obtengo sólo los 3 canales (b,g,r) de la imagen
logo_3_canales = logo[:,:,0:3]
# Defino el canal alfa con 3 canales
canal_alfa = cv2.merge((canal_alfa, canal_alfa, canal_alfa))
# Convierto la imagen a flotante para operar con ella
logo_3_canales = logo_3_canales.astype(float)
# Normalizar máscara Alfa para mantener intensidad entre 0 y 1
canal_alfa = canal_alfa.astype(float)/255.0

captura = cv2.VideoCapture('video1.mp4')
_, imagen = captura.read()
# Obtengo el alto y ancho del vídeo leído
h, w = imagen.shape[0:2]
cv2.waitKey(1000)

while True:
   
    (grabbed, frame) = captura.read()
    if not grabbed:
        break

    """ Agrego el ícono al vídeo en cada frame """
    # Coloco el ícono en la imagen
    ROI = frame[ (h-SIZE_ICON):h, (w-SIZE_ICON):w]
    ROI = ROI.astype(float)

    # Multiplicacion canal alfa y primer plano
    logo_3_canales = cv2.multiply(canal_alfa, logo_3_canales)

    # Multiplicacion fondo con (1 - canal alfa)
    ROI = cv2.multiply( (1.0 - canal_alfa), ROI)

    # Adición de logo_3_canales y fondo
    resultado = cv2.add(logo_3_canales, ROI)

    # Agrego la región a la imagen final
    frame[ (h-SIZE_ICON):h, (w-SIZE_ICON):w] = resultado

    # Muestro la imagen en el video
    cv2.imshow('Video', frame)
    # Capturamos la tecla
    tecla = cv2.waitKey(25) & 0xFF
    #Salimos si la tecla presionada es ESC
    if tecla == 27:
        break

    