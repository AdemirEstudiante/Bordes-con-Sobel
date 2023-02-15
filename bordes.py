import cv2
 
# Read the original image
img = cv2.imread('Tareas/tarea04/bordes.png') 
# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
 
# lo convierte a gris
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Aplica blur
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# deteccion de bordes
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) 
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) 

# se muestran las imagenes de la deteccion de borde
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y usando Sobel() funcion', sobelxy)
cv2.waitKey(0)
 
# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Imagen final
cv2.imshow('Deteccion de Bordes', edges)
cv2.waitKey(0)
 
cv2.destroyAllWindows()