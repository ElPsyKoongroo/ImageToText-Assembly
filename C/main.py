
size_bw = 200
size_color = 200

import cv2 as cv    #opencv-python
import numpy as np
from math import pow
import os

class ImageToText:

    _imagePath: str

    _ancho: int
    _alto: int

    def __init__(self, imagePath):
        '''
        imagePath               : ruta a la imagen
        color                   : 0 -> B&W, 1 -> Gray, 2 -> Color
        color_min y color_max   : tupla con los valores RGB de los colores que se quieren buscar (solo modo B&W)
        generateCode            : genera el codigo de la imagen para ensamblador
        showResult              : muestra la imagen original y la imagen con la máscara ya aplicada (solo modo B&W y Gray)
        showMatrix              : muestra la matriz de la imagen en consola (solo modo B&W)
        invert                  : invierte la seleccion en el resultado final (solo modo B&W)

        Cualquier variable que sea pasada por parametro y no sea necesaria sera ignorada
        '''

        if imagePath is None:
            raise Exception("imagePath es requerido")

        elif not os.path.exists(imagePath):
            raise Exception("imagePath no existe")

        elif not os.path.isfile(imagePath):
            raise Exception("imagePath no es un archivo")

        self._imagePath     = imagePath

    def Get_Image(self):
        
        img = cv.imread(self._imagePath)

        max = img.shape[1] if img.shape[1] > img.shape[0] else img.shape[0]

        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.cached_colors = {}
        out = False

        
        porcentaje = 85 / max
        self._ancho   = int(img.shape[1] * porcentaje)
        self._alto  = int(img.shape[0] * porcentaje)
        img2 = cv.resize(img, (self._ancho, self._alto), interpolation = cv.INTER_AREA)

        print(f"{self._alto}, {self._ancho}")

        with open("colors2.txt", "w+") as f:
            for i in range(self._alto):
                for j in range(self._ancho):
                    (r,g,b) = img2[i][j]
                    f.write(f"{r:03}{g:03}{b:03}")
                f.write("\n")
            
        return

if(__name__ == "__main__"):
    #[110, 110, 0], [255, 255, 255], (color azul)
    obj = ImageToText("arch.png", color=2)
    obj.Get_Image()