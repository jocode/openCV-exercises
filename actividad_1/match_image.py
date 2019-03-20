# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Obtengo el nombre de la plantilla que deseo encontrar en la imagen
imagen = str(raw_input('Ingrese el nombre de la imagen plantilla (.jpg): '))

# Leemos las dos imágenes, la original y la plantilla a escala de grises (0)
origin_color = cv2.imread('original.jpg', 1)
origin = cv2.cvtColor(origin_color, cv2.COLOR_BGR2GRAY)
template = cv2.imread(imagen+'.jpg', 0)

# Muestro las propiedades de la imagen origen
print("Dimensiones Original: ", origin.shape)
# Muestro las propiedades de la imagen template
print("Dimensiones Plantilla: ", template.shape)

# Compuebo que la imagen coincida con la cantidad total de pixeles de la original en (x,y)
if ( (origin.shape[0]%template.shape[0] == 0) and (origin.shape[1]%template.shape[1] == 0) ):
	print('El template coincide perfectamente con la original')

# Tamaño de la imagen Template
size_x = template.shape[0]
size_y = template.shape[1]

umbral_list = []

# Uso el ciclo for desde el 0 hasta la dimensión n en x, con un paso en x, definido por la imagen plantilla
for x in range(0, origin.shape[0], size_x):
	for y in range(0, origin.shape[1], size_y):
		# Defino la region de interés con las mismas dimensiones que la plantilla
		x1 = x + size_x
		y1 = y + size_y

		ROI = origin[x:x1, y:y1]

		# Realizo la resta absoluta entre imagen plantilla y ROI.
		resta_abs = cv2.absdiff(template, ROI)

		# Sumo el total de los pixeles de la imagen resultado de la resta absoluta
		suma_pix = np.sum(resta_abs)

		# Al imprimir estos números establezco un umbral. Por lo pronto lo dejaré en 2500, para redondear por encima (Probando con todas las imagenes)
		umbral_list.append(suma_pix)
		if (suma_pix < 2500):
			print('x ', x, ' x1 ', x1)
			print('y ', y, ' y1 ', y1)
			print('Suma pixeles ', suma_pix)

			# Dibujo un rectangulo en coordenadas (x, y) punto superior, (x1, y1) punto inferior, color rojo y un grosor de 3 px
			cv2.rectangle(origin_color, (x, y), (x1, y1), (0, 0, 255), 2)
			cv2.imshow('ROI MATCH', ROI)
		
print('El umbral ordenado es', sorted(umbral_list))
cv2.imshow('Resultado de Coincidencias', origin_color)
cv2.waitKey(0)
cv2.destroyAllWindows()