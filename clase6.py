"""numeroIngresado=[input("Por favor, ingrese 10 numeros: ")]
i=0
while i < 10
print (numeroIngresado)"""


#ejercicio de repetitivos con lista:
"""lista = []
for i in range(10):
    lista.append(int(input("ingrese un numero: ")))

maximo = max(lista)
print("el maximo de la lista es: "+ str(maximo))"""

#Magic 8-Ball
#El usuario hace una pregunta
#El programa le responde
#solo hasta 5 intentos
#salir 

#import random

#print("Bienvenido al juego")
#dato = str(input("hazme una pregunta "+ "n\ingresa 'salir' para finalizar el juego: "))

#i = 0

#while i <= 5 :

#    if dato == 'salir':
#       break

#    elif:
#    print(respuestas[random.randint(0,len(respuestas))]) 
#    respuestas = ["si", "no", "Es muy probable"]

#i + 1

#PEDIR AYUDA PORQUE ROMPÍ TODO 

###########################################
            
#LISTAS, TUPLAS, DICCIONARIOS- EJERCICIO  1
"""lista=[]
for x in range(5):
    nums = int(input('Ingrese 5 numeros:'))
    lista.append(nums)
 
print("Lista original", lista)
 
for x in range(0,len(lista)):
    lista[x]=lista[x]*lista[x]
 
print("El cuadrado de la lista es", lista
 """

#numero = int(input("Dígame cuántas palabras tiene la lista: "))
#
#if numero < 1:
#    print("¡Imposible!")
#else:
#    lista = []
#    for i in range(numero):
#        print("Dígame la palabra", str(i + 1) + ": ", end="")
#        palabra = input()
#        lista += [palabra]
#    print("La lista creada es:", lista)

nota = float(input("Ingresar una nota "))

if nota >= 9:
    print("sobresaliente")
elif nota >= 7:
    print("notable")
elif nota >= 6:
    print ("bien")
elif nota >= 5:
    print("insuficiente")


contraseña = "12345"
dato = (input("Por favor, ingrese su clave - recuerde que tiene 5 intentos: "))

i = 0

while dato != "12345":
    print("incorrecto, intente nuevamente")
    i +1
else:
    print("bienvenido")

