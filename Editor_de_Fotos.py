from PIL import Image
import numpy
from P1_funciones import *


#----90 GRADOS----#
def noventagrados(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")
    rotada = list()  # [[],[],[]]
    for linea in matriz:
        for pixel in linea:
            rotada.append([0,0,0])
    for linea in matriz:
        cont = 0
        for pixel in linea:
            rotada[cont].append(pixel)
            cont +=1
    convertirMatrizAImagen(rotada, "90-"+imagen)

            
#-----90 GRADOS RELOJ----#
def menosnoventagrados(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")
    rotada = list()       # [[],[],[]]
    for linea in matriz:
        rotada.append(list())
    for linea in matriz:
        cont = 0
        for pixel in linea:
            rotada[cont].append(pixel)
            cont +=1
    convertirMatrizAImagen(rotada, "90-V2"+imagen)
#menosnoventagrados()


#----BANDERA----#
def Bandera(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")
    cont = 0
    for linea in matriz:
        cont2 = 0
        for pixel in linea:
            R,G,B = pixel
            if cont<(len(matriz))/2 and cont2<=(len(linea))/2:
                B = 255
                pixel= [R,G,B]
                matriz[cont][cont2]=pixel
            if cont<=(len(matriz))/2 and cont2>(len(linea))/2:
                R += 200
                B += 200
                G += 200
                pixel= [R,G,B]
                matriz[cont][cont2]=pixel
            if cont>len(matriz)/2:
                R = 255
                pixel = [R,G,B]
                matriz[cont][cont2]=pixel
                
            cont2+=1
        cont+=1
    convertirMatrizAImagen(matriz, "Bandera-"+imagen)



#----BLANCO Y NEGRO-------#

def BlackAndWhite(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")
    
    cont= 0
    for linea in matriz:
        cont2 = 0
        for pixel in linea: #[R,G,B]
            R,G,B = pixel
            prom = int((R+G+B)/3)
            pixel2 = [prom,prom,prom]
            matriz[cont][cont2] = pixel2
            cont2 +=1
        cont+=1
    convertirMatrizAImagen(matriz, "B&W-"+imagen)

    
#----ESPEJO HORIZONTAL----#

def espejo_horizontal(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")
    for linea in matriz:
        linea.reverse()
    convertirMatrizAImagen(matriz, "reflejo-h-"+imagen)



#----ESPEJO VERTICAL----#
def espejo_vertical(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")
    matriz.reverse()
    convertirMatrizAImagen(matriz, "reflejo-v-"+imagen)


#----GLITCH----#

def Glitch(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")

    vertical = len(matriz)
    arriba = 0 + int(vertical/3)
    abajo = vertical - int(vertical/3)
    rango = (arriba,abajo)
    mov = int((len(matriz[0])/4))
    cont = 0
    cont2 = 0
    for linea in matriz:
        if cont < rango[1] and cont > rango[0]:
            while cont2 < mov :
                for pixel in linea:
                    matriz[cont].append(pixel)
                    matriz[cont].remove(pixel)
                    cont2 +=1
            cont2 = 0
        cont +=1
    convertirMatrizAImagen(matriz, "glitch-"+imagen)
    

#-----NEGATIVO----#

def Negativo(imagen):
    convertirImagenAArchivo(imagen,"matriz.txt")
    matriz = leerArchivo("matriz.txt")
    
    cont= 0
    for linea in matriz:
        cont2 = 0
        for pixel in linea: #[R,G,B]
            R,G,B = pixel
            RN = 255-R
            GN = 255-G
            BN = 255-B
            pixel2 = [RN,GN,BN]
            matriz[cont][cont2] = pixel2
            cont2 +=1
        cont+=1
    convertirMatrizAImagen(matriz, "negativo-"+imagen)    
