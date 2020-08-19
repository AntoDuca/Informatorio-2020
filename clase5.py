# COMPLEMENTARIOS - CONDICIONALES
# EJERCICIO 17
# Determinar y exhibir si la estatura de una persona adulta dada,
# es mayor que la estatura media de las personas adultas de su sexo,
# siendo:
# - estatura media de mujeres adultas: 1,65 m.
# - estatura media de varones adultos: 1,72 m.

"""estatura = float(input('Ingrese su estatura: '))
sexo = int(input('Ingrese segun corresponda su sexo: 1-Masculino 2-Femenino: '))

if estatura > float('1.72') and sexo == 1:
    print('La estatura es mayor a la media de varones adultos')
if estatura > float('1.65') and sexo == 2:
    print('La estatura es mayor a la media de mujeres adultas')"""

    #opc2

#Determinar y exhibir si la estatura de una persona adulta dada,
# es mayor que la estatura media de las personas adultas de su sexo, siendo:
#-estatura media de mujeres adultas: 1,65 m.
#-estatura media de varones adultos: 1,72 m.

"""estatura_m = str(input('La persona es una mujer adulta?'))

if estatura_m == 'si' :
    est = str(input('Ingrese la estatura: '))
    if est < '1,65' :
        print('La persona ingresada tiene una estatura menor a la media ')
    elif est > '1,65':
        print('La persona ingresada tiene una estatura mayor a la media')
    elif est == '1,65':
        print('La persona ingresada tiene una estatura igual a la media')

if estatura_m == 'no' :
    est_h = str(input('Ingrese la estatura de un varon adulto: '))
    if est_h < '1,72':
        print('La persona ingresada tiene una estatura menor a la media')
    elif est_h > '1,72':
        print('La persona ingresada tiene una estatura mayor a la media')
    elif est_h == '1,72':
        print('La persona ingresada tiene una estatura igual a la media')"""

#opc3

"""def altura_es_mayor_al_promedio(sexo, alto):
    altura_prom_sexo = 0
    print(sexo)
    print(sexo.upper() == "M")
    print(sexo.upper() == "F")
    if sexo.upper() == "M":
        altura_prom_sexo = 1.72
    elif sexo.upper() == "F":
        return "Error"
    print(altura_prom_sexo)
    if alt > altura_prom_sexo:
        return "La estatura es mayor al promedio de su sexo"
    else:
        return "La estatura es menor al promedio de su sexo"

    sexo = str(input("Ingrese el sexo de la persona: "))
    altura = float(input("Ingrese la altura de la persona: "))

    print(altura_es_mayor_al_promedio((sexo, altura)))"""

    #Programa original

def altura_es_mayor_al_promedio(sexo, alt):
    altura_prom_sexo = 0
    if sexo == "M":
        altura_prom_sexo = 1.72
    else:
        altura_prom_sexo = 1.65
    if alt > altura_prom_sexo:
        return "La estatura es mayor al promedio de su sexo"
    else:
        return "La estatura es menor al promedio de su sexo"

sexo =  str(input("ingrese el sexo de la persona: "))
altura = float(input("ingrese el altura de la persona: "))

print(altura_es_mayor_al_promedio(sexo, altura))