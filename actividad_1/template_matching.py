# -*- coding: utf-8 -*-
import cv2
import numpy as np 

opcion = int(raw_input("""
	¿Qué deseas hacer?
	[1] Comparar (1) imagen 
	[2] Comparar todas las imágenes

	: """))
if opcion == 1:
	iteracion = 1
	name_template = str(raw_input('Ingrese el nombre de la imagen (.jpg): '))
elif opcion == 2:
	iteracion = 4
else:
	print "Opcion incorrecta"
	exit()

imagen = cv2.imread('original.jpg', 1)
imagen_bn = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# División de la imagen Base en sus canales
b, g, r = cv2.split(imagen)
# Por si no entra al condicional
imagen_resultado = cv2.merge((b,g,r))

umbral = 20000

for indice in range(1, iteracion+1):

	if opcion == 1:
		template = cv2.imread(name_template+'.jpg', 0)
	else:
		print("Hola mundo", indice)
		template = cv2.imread(str(indice)+'.jpg', 0)
	
	width, height = template.shape[::-1] 

	for x in range(0, imagen_bn.shape[0], width):
		for y in range(0, imagen_bn.shape[1], height):
			# Defino las dimensiones del punto 2
			x1 = x + width
			y1 = y + height
			# Asigno el ROI para comparar los datos
			ROI = imagen_bn[x:x1, y:y1]
			# Realizo la resta absoluta entre imagen plantilla y ROI.
			resta_abs = cv2.absdiff(template, ROI)
			# La suma total de píxeles restantes es el umbral 
			suma_pix = np.sum(resta_abs)

			# Si el se cumple la condición, la imagen coincide en gran parte
			if (suma_pix < umbral):
				print('Umbral mínimo: ',suma_pix)
				print('x ', x, ' x1 ', x1)
				print('y ', y, ' y1 ', y1)
				# Asigno la imagen template en B&W a los canales de la imagen completa
				b[x:x1,y:y1] = template;
				g[x:x1,y:y1] = template;
				r[x:x1,y:y1] = template;
				
				font_size = 2
				tr = ((y+y1)/2)-(font_size*10)
				tc = ((x+x1)/2)+(font_size*10)
				cv2.putText(r, str(indice), (tr, tc), cv2.FONT_HERSHEY_SIMPLEX, font_size, (0, 0, 255), 2, cv2.LINE_AA)

				cv2.rectangle(b, (y, x), (y1, x1), (0, 0, 255), 3)
				cv2.rectangle(g, (y, x), (y1, x1), (0, 255, 0), 3)
				cv2.rectangle(r, (y, x), (y1, x1), (255, 0, 0), 3)
				# Dibujo un rectangulo en coordenadas (y, x) punto superior, (y1, x1) punto inferior, color rojo y un grosor de 3 px
				# Recordar que las filas son 'y' y las columas 'x'
				imagen_resultado = cv2.merge((b,g,r))


cv2.imshow('Resultado de Coincidencias', imagen_resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()