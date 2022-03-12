#import cv2 as cv
#import numpy as np
#
#img = cv.imread("fotos/colores.png")
#
##dic: dict = {}
#lista: list = []
#
#for i in range(256):
#    color = int(img[0][i*2][0]/32) << 5 | int(img[0][i*2][1]/32) << 2 | int(img[0][i*2][2]/64)
#    lista.append(color)
#    #dic[color] = i
#
#with open("colores.py", "w") as f:
#    #f.write("colores = [\n")
#    #for i in dic:
#    #    f.write("{},\n".format(i))
#    #f.write("]\n")
#    #dics = json.dumps(dic)
#    #dics = "colores = " + str(dic)
#    #f.write(dics)
#
#    #for x in lista:
#        #f.write("{}:{},\n".format(x,y))
#    f.write("colors = " + str(lista))
#

for sz in range(200, 0, -1):
    print(sz)