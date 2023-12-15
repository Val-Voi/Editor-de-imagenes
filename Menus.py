from PIL import Image
import numpy
from P1_funciones import *
from Editor_de_Fotos import *



print ('Instrucciones:')
print ('-Para cargar una imagen,escriba su nombre incluyendo su extension')
print (' Ejemplo: imagen.png')
print ('-Para salir dejar en blanco')


while True:
    imagen = input('Nombre del archivo: ')
    if imagen == '':
        break
    if imagen != '':
        print ('Lista de filtros disponibles:')
        print ('1.- Blanco y Neegro')
        print ('2.- Negativo')
        print ('3.- Glitch')
        print ('4.- Espejo Horizontal')
        print ('5.- Espejo Vertical')
        print ('6.- Bandera')
        print ('7.- Rotacion 90 Grados (Sentido Horario)')
        print ('8.- Rotacion 90 Grados (Sentido Antihorario')
        print ('10.- Cargar otra imagen')

        opcion = input("Elija una de las opciones anteriores: ")
        while opcion != '10':
            if opcion == "1":
                BlackAndWhite(imagen)
            if opcion == "2":
                Negativo(imagen)
            if opcion == "3":
                Glitch(imagen)
            if opcion == "4":
                espejo_horizontal(imagen)
            if opcion == "5":
                espejo_vertical(imagen)
            if opcion == "6":
                Bandera(imagen)
            if opcion == '7':
                noventagrados(imagen)
            if opcion == '8':
                menosnoventagrados(imagen)
            opcion = input("Elija una de las opciones anteriores: ")
