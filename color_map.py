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
from colores import *
import cv2 as cv
import numpy as np

input = [85, 255, 245]
colores = colors

 #find the closest rgb color in a list of colors
def closest_colour(requested_colour):
    min_colours = {}
    for name in colores:
        r_c, g_c, b_c = name
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

print(closest_colour(input))

print(colores.index(closest_colour(input)))


'''



67 B7 46

67 86 46

67 87 49



'''