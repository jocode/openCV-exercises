# -*- coding: utf-8 -*-
import cv2 
import numpy as np 
import math

# Valores de monedas guardados de area mas grande a mas pequeña
VALUES_COINS = {
    0: (200, (36,36,255)),
    1: (500, (0,126,253)),
    2: (100, (255,0,255)),
    3: (50, (255,255,0)),
    4: (20, (255,0,0)),
    5: (10, (0,255,255)),
    6: (5, (0,255,0))
}

rango_areas = [(10219.0, 10658.0), (9560.0, 10044.0), (9221.0, 9540.0), (8040.0, 8413.0), (6985.0, 7324.0), (6054.0, 6322.0), (5151.0, 5402.0)]

# Cargo la imagen
img = cv2.imread('images/test1.jpeg')

# 1. Se convierte la imagen a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Escala de grises', gray)

# 2. Se elimina el ruido usando el filto gaussiano
filtro = cv2.GaussianBlur(gray, (3,3), 0)
cv2.imshow('Imagen Filtrada - Filtro Gaussiano', filtro)

# 3. Deteccion de bordes Canny
bordes  = cv2.Canny(filtro, 20, 150)
cv2.imshow('Bordes Canny', bordes)

# 4. Se realizala operación morfológica para rellenar espacios
bordes = cv2.dilate(bordes, None, iterations=2)
bordes = cv2.erode(bordes, None, iterations=1)
cv2.imshow('Operación Morfológica', bordes)

# 5. Búsqueda de contornos  externos
_, cnts, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(VALUES_COINS)

# 6. Recorrido de cada uno de los contrornos
i = 0
total = 0
for cnt in cnts:
    # 7. Se calcula el area de los contornos
    area = cv2.contourArea(cnt)
    
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        break

    # 8. Se dibujan los contornos
    """ Para dibujar contornos, siempre es necesario pasar el contorno entre corchetes angulares [contorno] """

    for idx, rango in enumerate(rango_areas):
        if (rango[0] < area < rango[1]):
            print("El valor es de {} en el rango {}".format(VALUES_COINS[idx][0], rango))
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            centro = (int(x),int(y))
            valor = str(VALUES_COINS[idx][0])
            cv2.drawContours(img, [cnt], -1, VALUES_COINS[idx][1], 2)
            cv2.circle(img,centro,3,(0,0,255),-1)
            cv2.putText(img, valor, centro, cv2.FONT_HERSHEY_DUPLEX , 0.6, (255,0,0))
            total += VALUES_COINS[idx][0]

    cv2.imshow('Resultado', img)
    print(area)
    i += 1


print('El numero de monedas es {} para un valor de {}'.format(i, total))
cv2.waitKey(0)
cv2.destroyAllWindows()