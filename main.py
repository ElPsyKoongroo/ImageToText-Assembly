'''
Depencencias: (instala estos dos paquetes si te dice que no estan instalados mediante 'pip install {nombre de paquete}' en la terminal)
    opencv-python
    numpy

Funcionamiento:
    Al principio del constructor (linea x) puedes ver qué significa cada argumento.

    Cuando vayas a crear el objeto (hay uno de ejemplo), si le quieres pasar cualquier argumento extra (los que no tienen un default),
    lo puedes poner de dos formas:

        -Todos, en el mismo orden que en el constructor

        -nombre_del_argumento = valor_del_argumento, para no tener que ponerlos todos

    https://imagecolorpicker.com/es
        Con esta pagina puedes pillar los colores de la imagen para ponerlo despues en los argumentos del constructor

'''

inicio = '''.model small
.code

    mov al, 13h
    mov ah, 0
    int 10h

    mov ax, 0A000h
    mov es, ax

    mov ax, 0Fh; Color con el que se rellena el dibujo
    jmp start

line:
    mov dx, 0

line_loop:
    mov es:[bx], al
    inc dx
    inc bx
    cmp dx, cx
    jne line_loop
    ret

_lineMacro MACRO p1, p2, p3
    mov bx, p1
    mov cx, p2
    mov ax, p3
    call line
ENDM

start:

'''

final = '''
    mov ah, 4Ch
    int 21h
end'''

size_bw = 200
size_color = 120

import cv2 as cv    #opencv-python
import numpy as np  #numpy
from colores import colors as color_map

class ImageToText:

    _imagePath: str
    _color_minimo: tuple
    _color_maximo: tuple
    _text: int
    _size: int
    _matrix = []

    _genCode: bool
    _showResult: bool
    _showMatrix: bool

    _ancho: int
    _alto: int

    _color: bool
    _img: np.ndarray

    def __init__(self, imagePath, color_min = None, color_max = None, color = False, generateCode = False, showResult = False, showMatrix = False, invert = False):
        '''
        imagePath               : ruta a la imagen
        color_min y color_max   : tupla con los valores RGB de los colores que se quieren buscar
        color                   : si es True, se genera en color, si es False, se genera B&W
        generateCode            : genera el codigo de la imagen para ensamblador
        showResult              : muestra la imagen original y la imagen con la máscara ya aplicada
        showMatrix              : muestra la matriz de la imagen en consola
        invert                  : invierte la seleccion en el resultado final (prueba si no estas seguro)
        '''
        self._imagePath     = imagePath
        self._color_minimo  = color_min
        self._color_maximo  = color_max
        
        self._text = 1 if invert else 0

        self._showResult    = showResult
        self._genCode       = generateCode
        self._showMatrix    = showMatrix
        self._color         = color
        self._size = size_color if color else size_bw

    def ShowMatrix(self):
        for i in range(self._alto):
            for j in range(self._ancho):
                if(self._matrix[i][j] == self._text):
                    print("  ", end="")
                else:
                    print("* ", end="")
            print()

    def ShowImage(self, original, mod):

        cv.imshow("Imagenes", np.hstack([original, mod]))
        cv.waitKey(0)
        cv.destroyAllWindows()

    def GenerateCodeBW(self):
        toWrite = (pos_i*320+pos_j for pos_i, i in enumerate(self._matrix) for pos_j, j in enumerate(i) if j == self._text)

        offset = 320 - self._ancho

        #f.write("    mov es:[{}], al\n".format(i+offset))
        with open("main.asm", "w") as f:
            f.write(inicio)
            cont = 0
            first = -1
            for i in toWrite:
                
                if(cont == 0):
                    first = i
                
                if(i-cont == first):
                    cont+=1
                    continue

                f.write("    mov cx, {}\n".format(cont))
                f.write("    mov bx, {}\n".format(first+offset))
                f.write("    call line\n")
                cont = 0


            f.write(final)

    def MatrixBW(self, img, output):
        for i in range(self._alto):
            self._matrix.append([])
            for j in range(self._ancho):
                if (output[i][j][0] != 0 or output[i][j][1] != 0 or output[i][j][2] != 0):
                    self._matrix[i].append(1)
                else:
                    self._matrix[i].append(0)

        if self._showResult:
            self.ShowImage(img, output)
        if self._showMatrix:
            self.ShowMatrix()

        if self._genCode:
            self.GenerateCodeBW()

    def Get_Image(self):
        
        img = cv.imread(self._imagePath)



        #cv.imshow("Imagenes", cv.cvtColor(cv.resize(img, (500, 750), interpolation = cv.INTER_AREA), cv.COLOR_BGR2GRAY))
        #cv.waitKey(0)

        max = img.shape[1] if img.shape[1] > img.shape[0] else img.shape[0]

        porcentaje = self._size / max

        self._ancho   = int(img.shape[1] * porcentaje)
        self._alto  = int(img.shape[0] * porcentaje)

        dim = (self._ancho, self._alto)

        img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

        if(self._color):
            self.ColorMatrix(img)
            return

        minimo = np.array(self._color_minimo, dtype = "uint8")
        maximo = np.array(self._color_maximo, dtype = "uint8")

        mask = cv.inRange(img, minimo, maximo)
        output = cv.bitwise_and(img, img, mask = mask)
        
        self.MatrixBW(img, output)

    def GenerateCodeColor(self):
        toWrite = ((pos_i*320+pos_j, j) for pos_i, i in enumerate(self._matrix) for pos_j, j in enumerate(i))
        #_lineMacro
        #name = f"{self._imagePath.split('.')[0]}_c.asm"
        offset = 320 - self._ancho
        with open("output.asm", "w") as f:
            f.write(inicio)
            cont = 0
            #totalLines = 0
            for pos, color in toWrite:
                if(cont == 0):
                    first = pos
                    actual = color
                
                if(pos-cont == first and color == actual):
                    cont+=1
                    continue

                #f.write("    mov al, {}d\n".format(actual))
                #f.write("    mov cx, {}\n".format(cont))
                #f.write("    mov bx, {}\n".format(first+offset))
                #f.write("    call line\n")

                f.write("   _lineMacro {}, {}, {}\n".format(first+offset, cont, actual))
                cont = 1
                actual = color
                first = pos

                #totalLines+=1
                #if(totalLines == 2000):
                #    f.write(".code _{}\n".format(totalLines))
                #    totalLines = 0

            print(offset)
            f.write(final)

        '''toWrite = ((pos_i*320+pos_j, j) for pos_i, i in enumerate(self._matrix) for pos_j, j in enumerate(i))

        name = f"{self._imagePath.split('.')[0]}_c.asm"
        offset = 320 - self._ancho
        with open(name, "w") as f:
            f.write(inicio)
            actual: int = -1
            for pos, color in toWrite:
                if(color != actual):
                    actual = color
                    f.write("    mov al, {}d\n".format(color))

                f.write("    mov es:[{}], al\n".format(pos+offset))
            f.write(final)'''

    def ColorMatrix(self, img):

        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


        for i in range(self._alto):
            self._matrix.append([])
            for j in range(self._ancho):

                #r: int = int(img[i][j][0])
                #g: int = int(img[i][j][1])
                #b: int = int(img[i][j][2])

                #color = (r*6/256)*36 + (g*6/256)*6 + (b*6/256)
                #color = ( r << 5) | ( g << 2 ) | ( b )
                #while color not in color_map:
                #    color += 1
                #color = color_map.index(color)

                final_color = 16
                aux = 16
                color = img[i][j]

                while color > aux:
                    final_color += 1
                    aux += 16


                self._matrix[i].append(final_color) # & 0xffffffff

        if self._genCode:
            self.GenerateCodeColor()

if(__name__ == "__main__"):
    #[110, 110, 0], [255, 255, 255], (color azul)
    obj = ImageToText("fotos/Foticos.jpg", color=True, generateCode=True)
    obj.Get_Image()