# Template Matching

La Template matching (comparación de plantillas) es una técnica para encontrar áreas de una imagen que son similares a un patrón (plantilla).

Un patrón es una imagen pequeña con ciertas características. El objetivo de la comparación de plantillas (Template Matching) es encontrar el patrón/plantilla en una imagen.

Para encontrarlo, el usuario tiene que dar dos imágenes de entrada: Imagen de origen (S) – La imagen para encontrar la plantilla y  la Imagen de plantilla (T) – La imagen con cierto atributo que se encuentra en la imagen de origen.



## 1. ¿Qué es Template Matching?


Template Matching es básicamente un método para buscar y encontrar la ubicación de una imagen de plantilla en una imagen más grande.

La idea aquí es encontrar regiones idénticas de una imagen que coincidan con una plantilla que proporcionamos, dando un umbral (threshold)

- El umbral depende de la precisión con la que queremos detectar la plantilla en la imagen de origen.
- Por ejemplo, si aplicamos el reconocimiento facial y queremos detectar los ojos de una persona, podemos proporcionar una imagen aleatoria de un ojo como la plantilla y buscar la fuente (la cara de una persona).
- En este caso, ya que los “ojos” muestran una gran cantidad de variaciones de persona a persona, incluso si fijamos el umbral como 50% (0.5), el ojo será detectado.
- En los casos en que se busquen plantillas casi idénticas, el umbral debe fijarse alto. (T> = 0.8)



## ¿Cómo funciona el Template Matching?

- La imagen de la plantilla simplemente se desliza sobre la imagen de entrada (como en la convolución 2D)
- Ésta plantilla creada (de la imagen de entrada) y la imagen de plantilla se comparan.
- El resultado obtenido se compara con el umbral.
- Si el resultado es mayor que el umbral, la porción será marcada como detectada.
- En la función cv2.matchTemplate (img_gray, template, cv2.TM_CCOEFF_NORMED) el primer parámetro es la imagen principal, el segundo parámetro es la plantilla a emparejar y el tercer parámetro es el método utilizado para hacer coincidir.

*Para más info ver* [Template Matching usando OpenCV en Python](https://adictec.com/template-matching-usando-opencv-en-python/)


*Guía de la documentación oficial* [Template Matching ](https://docs.opencv.org/3.2.0/d4/dc6/tutorial_py_template_matching.html)

- **Funciones a utilizar**

	- cv2.imread() 
	- cv2.merge() 
	- cv2.rectangle() 
	- cv2.absdiff()
	- cv2.imshow()
	- cv2.waitKey() 
	- cv2.destroyAllWindows() 
	- np.sum()

