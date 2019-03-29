# -*- coding: utf-8 -*-
import cv2
import numpy as np 

# Lectura de las imagenes
primer_plano = cv2.imread('primer_plano.png')
fondo = cv2.imread('fondo.jpg')
canal_alfa = cv2.imread('canal_alfa.png')

# Imprimir las formas de las imágenes
print('Datos de las imágenes originales')
print('Primer plano ', primer_plano.shape)
print('Fondo ', fondo.shape)
print('Canal alfa ', canal_alfa.shape)

# Redimensionamos las imágenes a 600*400, 
primer_plano = cv2.resize(primer_plano, (600, 400))
fondo = cv2.resize(fondo, (600, 400))
canal_alfa = cv2.resize(canal_alfa, (600, 400))

print('Datos de las imágenes redimensionadas')
# Recordar de openCV miuestra primero el alto y luego el ancho
print('Primer plano ', primer_plano.shape)
print('Fondo ', fondo.shape)
print('Canal alfa ', canal_alfa.shape)

# Convertimos las imágenes, en imágenes de punto flotante
primer_plano = primer_plano.astype(float)
fondo = fondo.astype(float)

# Normalizar máscara Alfa para mantener intensidad entre 0 y 1
canal_alfa = canal_alfa.astype(float)/255.0

# Multiplicacion canal alfa y primer plano
primer_plano = cv2.multiply(canal_alfa, primer_plano)

# Multiplicacion fondo con (1 - canal alfa)
fondo = cv2.multiply( (1.0 - canal_alfa), fondo)

# Adición de primer_plano y fondo
resultado = cv2.add(primer_plano, fondo)

cv2.imshow("Fusion", (resultado/255) )
cv2.waitKey(0)
cv2.destroyAllWindows()