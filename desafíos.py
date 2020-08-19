#1- emitir un mensaje de acuerdo a lo que una persona ingresa como cantidad de años que viene usando insecticida en su 
#plantación. Si hace 10 o más años, debemos emitir el mensaje "Por favor solicite revisión de suelos en su plantación". 
#Si hace menos de 10 años, debemos emitir el mensaje "Intentaremos ayudarte con un nuevo sistema de control de plagas, 
# y cuidaremos el suelo de tu plantación".
"""
print("┊"*30)
print("┊"*8,"Bienvenido/a","┊"*8)
print("┊"*30)
print("┊Por favor introducir el año ┊\n┊en que comenzó a utilizar   ┊\n┊insecticida                 ┊")
print("┊"*30)
valor1 = int(input("          año: "))
suma = 2020 - valor1
print("┊"*30)
print("┊La cantidad de años de uso  ┊\n┊de insecticida es de: ",suma,"  ┊")
print("┊"*30)
if suma >= 10:
    print("┊Por favor solicite revisión ┊\n┊de suelos en su plantación  ┊")
elif suma <= 9:
    print("┊Intentaremos ayudarte con un┊\n┊nuevo sistema de control de ┊\n┊plagas, y cuidaremos el     ┊\n┊suelo de tu plantación      ┊")
else:
    print("Gracias por utilizar el programa")
print("┊"*30)
"""

#2 
"""
tamañoNormal= "Pez en buenas condiciones"
tamañopordebajodeloNormal= "Pez con problemas de nutrición"
tamañounpocoporencimadeloNormal= "Pez con síntomas de organismo contaminado"
tamañosobredimensionado= "Pez contaminado"
medida = str(input("________Califique el tamaño del pez______\n\n(Introducir el numero que corresponda)\n1- Normal\n2-Pequeño\n3- Extragrande\n4- Sobredimencionado\n"))
if medida == "1":
    print(tamañoNormal)
elif medida == "2":
    print(tamañopordebajodeloNormal)
elif medida == "3":
    print(tamañounpocoporencimadeloNormal)
elif medida == "4":
    print(tamañosobredimensionado)
else:
    print("Opción ingresada inválida")
"""

#3 Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto 
# en el suelo el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe 
# existir vegetación del tipo MATORRAL. Escribir un programa que determine si es factible 
# la utilización de fertilizantes.
"""
print("\n\nA continuación calcularemos si en su campo\n   es factible el uso de fertilizantes\n")
condicion1= str(input("¿En el terreno existe vegetación\ntipo matorral?\n"))
if condicion1 == "si":
    print("No debe utilizar fertilizante.")
elif condicion1 == "no":
    terreno = int(input("¿En cuántas hectáreas desea utilizar fertilizante?\n: "))
    condicion2 = terreno * 100 / 10
    if condicion2 >= 10:
        print("El compuestro por hectárea es de: ", condicion2,"%")
        print("Es factible el uso de ferttilizantes.")
    elif condicion2 <= 9:
        print("El compuestro por hectárea es de: ", condicion2,"%")
        print("No es factible el uso de fertilizantes.")
else:
    print("Opción ingresada inválida")
"""

#4 Tenemos que decidir entre 2 recetas ecológicas. 
# Los ingredientes para cada tipo de receta aparecen a continuación.
"""
Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morrón y Cebolla..
"""
#Escribir un programa que pregunte al usuario que tipo de receta desea, 
# y en función de su respuesta le muestre un menú con los ingredientes 
# disponibles para que elija. Solo se puede eligir 3 ingrediente (entre 
# la receta elegida y los comunes.) y el tipo de receta. Al final se debe 
# mostrar por pantalla la receta elegida y todos los ingredientes.

print("Bienvenido a tu menú ecológico.")
plato = str(input("¿qué plato desea hoy?\n-sopa de verduras 🌱 -verduras al vapor 🌿\n"))

if plato == "sopa de verduras":
    print("¡Exelente elección!🌱")
    ing = int(input("Selecciona los ingredientes que desea añadir:\n1- lentejas\n2- apio\n"))
    listaIng = []
elif plato == "verduras al vapor":
    print("¡Exelente elección!🌿")

#########################################################################################

"""print("Bienvenido al programa de identificación de peces")

tamañoDelPez = int(input("Ingrese en cm, el tamaño del pez a estudiar: "))

tamañoNormal =250
tamañoSdimensionado = 350

if tamañoDelPez < tamañoNormal:
    print("Pez cn problemas de nutrición")
elif tamañoDelPez == tamañoNormal:
    print("Pez en buenas condiciones")
elif tamañoDelPez > tamañoNormal:
    print("Pez con síntomas de organismo contaminado")
elif tamañoDelPez > tamañoSdimensionado:
    print("Pez contaminado")
else:
    print("Valor ingresado es inválido")"""

"""
La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.
"""

#Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.

"""nombre_barrio = input("Ingrese el nombre de su barrio >>> Bº: ")
ubicacion = int(input("Si el barrio donde vive es CÉNTRICO ingrese 1 o 2 si es NO CÉNTRICO: "))
if ubicacion == 1:
    if nombre_barrio < "M":
        print("Sección A")
    else:
        print("Sección B")
elif ubicacion == 2:
    if nombre_barrio >= "M":
        print("Sección A")
    else:
        print("Sección B")
else:
    print("Opción Incorrecta")"""