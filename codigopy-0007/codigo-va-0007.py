# Alexandro Aguilar Valadez NC = 0007

import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
carpeta_proyecto = Path(__file__).resolve().parent.parent

ruta_original = (
    carpeta_proyecto
    / "img-original-0007"
    / "Leon.jpg"
)

carpeta_resultados = (
    carpeta_proyecto / "resultados-img-0007"
)

# Crear la carpeta de resultados si no existe
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0007 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img0007 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_0007 = cv2.rotate(
    img0007, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0007.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0777 = cv2.warpAffine(
    img0007,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho
# y 500 píxeles de alto
img600x500_0007 = cv2.resize(
    img0007, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200
# píxeles sobre una copia de la imagen original
img_rojo_0007 = img0007.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0007,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("Leon original 0007 ", img0007)

cv2.imshow("Leon 90 0007", img90_0007)

cv2.imshow("Leon 45 0007", img45_0777)

cv2.imshow(
    "Leon 600x500 0007",
    img600x500_0007
)

cv2.imshow("Leon rojo 0007", img_rojo_0007)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "img-Leon1-0007.jpg"),
    img90_0007
)

cv2.imwrite(
    str(carpeta_resultados / "img-Leon2-0007.jpg"),
    img45_0777
)

cv2.imwrite(
    str(carpeta_resultados / "img-Leon3-0007.jpg"),
    img600x500_0007
)

cv2.imwrite(
    str(carpeta_resultados / "img-Leon4-0007.jpg"),
    img_rojo_0007
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Programa realizado por Alexandro Aguilar NC = 0007")