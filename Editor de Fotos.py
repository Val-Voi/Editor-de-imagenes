from PIL import Image
import numpy


#Escala de Grises : Promedio
#Negativo : 255- color

def convertirImagenAArchivo(nombreImagen, nombreDestino):
    imagen = Image.open(nombreImagen)
    imagen = imagen.convert('RGB')
    matrizNumpy = numpy.array(imagen)
    archivo = open(nombreDestino, 'w')
    for fila in matrizNumpy:
        for pixel in fila :
            for componente in pixel :
                archivo.write(' ' + str(componente))
            archivo.write(',')
        archivo.write('\n')
    archivo.close()
    return True

def leerArchivo(nombreEntrada):
    archivo = open(nombreEntrada,'r')
    matriz = []
    for i in archivo:
        lista = []
        fila = []
        lista = i.strip(",\n").split(',')
        for pixel in lista :
            aux = pixel.split()
            for e in range(3) :
                aux[e] = int(aux[e])
            fila.append(aux)
        matriz.append(fila)
    return matriz

def convertirMatrizAImagen(matriz, nombreSalida):
    arr = numpy.array(matriz)
    im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
    im.save(nombreSalida)
    return True


def espejo_vertical():
    convertirImagenAArchivo("Seesmic_Logo.png","matriz.txt")
    matriz = leerArchivo("matriz.txt")
    for linea in matriz:
        linea.reverse()
    convertirMatrizAImagen(matriz, "reflejo-v.png")

#espejo_vertical()



def BlackAndWhite():
    convertirImagenAArchivo("Seesmic_Logo.png","matriz.txt")
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
    convertirMatrizAImagen(matriz, "blackandwhite.png")

#BlackAndWhite()

def Negativo():
    convertirImagenAArchivo("Seesmic_Logo.png","matriz.txt")
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
    convertirMatrizAImagen(matriz, "negativo.png")

#Negativo()


def Glitch():
    convertirImagenAArchivo("Seesmic_Logo.png","matriz.txt")
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
    convertirMatrizAImagen(matriz, "glitch.png")
    
            
            



Glitch()


















    












            
            
    
    




























