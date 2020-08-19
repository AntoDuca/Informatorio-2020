#EL CÓDIGO FUNCIONA, PERO TE PIDE INGRESAR 2 VECES LA OCIÓN DE PIZZA.
#ADEMÁS QUIERO QUE ENTRE EN EL else CUANDO SE INTRODUZCA UN str(), PERO NO LO HACE
"""
print("Pizzería Bella Napoli")
opc = int(input("¿Qué tipo de pizza desea? \n 1- Vegetariana \n 2- No vegetariana "))

while opc !=1 or opc !=2:
    print("Intenta nuevamente")
    opc = int(input("¿Qué tipo de pizza desea? \n 1- Vegetariana \n 2- No vegetariana "))
    
    if opc == 1 or 2 :
     break

if opc == 1:
    print("¡Buena elección! \n Los ingresientes VEGETARIANOS disponibles son: \n Introduce el numero correspondiente según el ingrediente que desee añadir ")
    ingVeg= int(input("1- Pimiento \n 2- Rúcula \n "))

    if ingVeg == 1:
        print("Su pizza está lista \n Info nutricional: \n 256 kcal \n 41% carbh \n 19% prot \n Ingredientes: Pimiento, mozzarella y tomate")
    elif ingVeg == 2:
        print("Su pizza está lista \n Info nutricional: \n 250 kcal \n 21% carbh \n 10% prot \n Ingredientes: Rúcula, mozzarella y tomate")

elif opc == 2:
    print("¡Buena elección! \n Los ingresientes NO VEGETARIANOS disponibles son: \n Introduce el numero correspondiente según el ingrediente que desee añadir ")
    ingNoVeg= int(input("1- Jamón  \n 2- Panceta \n "))
    if ingNoVeg == 1:
        print("Su pizza está lista \n Info nutricional: \n 206 kcal \n 46% carbh \n 19% prot \n Ingredientes: Jamón, mozzarella y tomate")
    elif ingNoVeg == 2:
        print("Su pizza está lista \n Info nutricional: \n 200 kcal \n 29% carbh \n 23% prot \n Ingredientes: Panceta, mozzarella y tomate")

else:
    print("Código incorrecto")
"""

#Estudiantes de un curso se han dividido en dos grupos A y B de acuerdo al turno y el
#nombre. 
# El grupo A está formado por estudiantes del turno Tarde con un nombre anterior
#a la M y estudiantes del turno Noche con un nombre posterior a la N 

# y el grupo B por el
#resto. Escribir un programa que pregunte al usuario su nombre y turno, y muestre por
#pantalla el grupo que le corresponde.

"""
print("Bienvenido alumno, identifícate")

nombre= (input("Nombre: "))
turno = (input("Turno: mañana, tarde o noche\n "))

print("-" * 40, "\n", "-" * 10,"Datos Ingresados", "-" * 10," \n","-" * 40, "\n \n* Nombre del alumno:",nombre, "\n* Turno cursado de la carrera: ",turno, "\n")
listaM = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
listaN = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Inicial = nombre
Inicial = nombre[0]

if  Inicial in listaM and turno == "tarde":
    print("-" * 40, "\n", "\nPertenece al grupo *A* ", "\n")

elif Inicial in listaN and turno == "noche":
    print("-" * 40, "\n", "\nPertenece al grupo *A* ", "\n")

else:
    print("-" * 40, "\n","\nPertenece al grupo *B* ", "\n")
"""


#Solicite al usuario el ingreso de 3 números, 
# e imprímalos de mayor a menor.

"""print("Bienvenido usuario")
num1 = int(input("Por favor, ingresa un número: "))
num2 = int(input("Por favor, ingresa otro número: "))
num3 = int(input("Por favor, ingresa el tercer número: "))
print(num1," ", num2, " ", num3)

if num1 > num3 and num1 > num2:
       print ("El numero mayor es: ", num1)

elif num2 > num1 and num2 > num3:
        print("El numero mayor es: ", num2)

else:
    print("El numero mayor es: ", num3)"""

#Desarrolle un programa que permita determinar 
#si un número X ingresado
#es par o impar.

"""num = int(input("Ingresa un numero entero: "))

if num % 2 == 0 :
    print("El numero ingresado es par")
else :
    print("El numero ingresado NO es par.")"""


#Determinar si el primero de un conjunto de tres números dados, 
#es menor que los otros dos

"""num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa un numero entero: "))
num3 = int(input("Ingresa un numero entero: "))

conjunto = ()
conjunto = (num1, num2, num3)

print(conjunto)

if num1 > num2 and num1 > num3:
    print("el numero mayor de la lista: ", conjunto, " es: \n", num1)
else:
    print("El primer numero de la lista ", conjunto, "NO ES EL MAYOR")"""

################################################################################



