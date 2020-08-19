#Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B.
#  El programa no permitirá introducir valores negativos para A y B 
# y verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
"""
num_a=int(input("Introduzca un número: "))
num_b=int(input("Introduzca un número mayor al anterior: "))
suma=0
      
for x in range(num_a, num_b+1):
        if x % 5 == 0:
                suma += x

print(for in range(num_a, num_b+1)
       
print("la suma entre los múltiplos de 5 que hay entre los valores A y B es", suma)
"""

# Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada 
# componente sea igual al cuadrado del componente original. El programa mostrara la lista resultante 
# por pantalla.
"""
lista=[]
for n in range(5):
    lista.append(int(input('Ingrese valor: \n')))
for n in range(5):
    lista[n] = lista[n]*lista[n]
print(lista)
"""

######################################################################
#HACER MATRICES Y PEDIR VALORES
"""matriz = []
filas = int(input("cantidad de filas: "))
columnas = int(input("cantidad de columnas: "))

for i in range(filas):
    matriz.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input("Elemento %d, %d : " % (f,c)))

print(matriz)"""

######################################################################
#ord("a")
#>>> 97
########POSICIÓN EN LA TABLA ASCII
#chr(97)
#>>> "a"

"""codSecreto = [70, 101, 108, 105, 122, 32,115,101,109,97,110,97,32,100,101,32,108,97,32,100,117,108,122,117,114,97]
for c in codSecreto:
    print("%s : %i" % (chr(c), c))"""
######################################################################

#from math import sqrt

#raizCuadrada = sqrt(93474739)
#print(raizCuadrada)

######################################################################

"""from random import *

fila = int(input('Ingrese numero de filas \n'))
columna = int(input('Ingrese numero de columnas \n'))

matriz = [[randint(1,100) for i in range(fila)] for j in range(columna)]
print(matriz)
print(type(fila))
print(type(columna))

for n in range(columna):
    print(matriz[n],end=' '"\n")
print()"""

######################################################################
"""lista = []
for x in range(5):
    nums = int(input("Ingrese 5 números: "))
    lista.append(nums)

print("Lista original: ", lista)

for x in range(0,len(lista)):
    lista[x]-lista[x]*lista[x]
    
print("El cuadrado de la lista es: ", lista)"""

def num_pulsaciones(edad):
    return "Sus pulsaciones deberían ser:", 220 - edad / 10
     
print(num_pulsaciones(22))
##########################################
def num_pulsaciones(edad):
    return (220 - edad) / 10

edad = int(input("Ingrese su edad: "))
print ("Sus pulsaciones deberían ser: ", num_pulsaciones(edad))