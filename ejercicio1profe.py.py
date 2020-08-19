### EJERCICIO 1
### DADO UN NUMERO INGRESADO, IMPRIMIR TODOS LOS NUMEROS DEL 1 AL NUMERO
### INGRESADO ELEVADOS AL CUADRADO
### RESULTADO
### SI INGRESO 1 ==> RESULTADO: 1
### SI INGRESO 2 ==> RESULTADO: 1 2
### SI INGRESO 3 ==> RESULTADO: 1 2 9
### SI INGRESO 4 ==> RESULTADO: 1 2 9 16
### SOLUCION (PUEDEN AGREGARLE MENSAJITOS :P)
n = int(input())
for i in range(n +1):
  print(i**2)


# EJERCICIO 2
### (1) - IMPRIMIR LA PRIMER LETRA DE LA VARIABLE PALABRA (SIN USAR EL OPERADOR "+")
### (2) - IMPRIMIR LA SEGUNDA, CON OTRO FORMA DE IMPRESION QUE NO SEA LA (1)
### (3) - IMPRIMIR LA TERCERA, CON OTRO FORMA DE IMPRESION QUE NO SEA LA (1) O (2)
palabra = "Informatorio"
print("La primer letra de Informatorio es: ", palabra[0]) #(1)
print(f"La segunda letra de Informatorio es: {palabra[1]}") #(2)
print('La tercer letra es, %s' % palabra[2]) #(3)

### EJERCICIO 3
### Usar las distintas formas de formatear string del ejercicio 3, para concatenar
### las variables primer_nombre y apellido
primer_nombre = "Juan"
apellido = "Perez"
print("Primer Nombre: " + primer_nombre + " Apellido: " + apellido)
print(f"Primer Nombre: {primer_nombre} Apellido: {apellido}")
print("Primer Nombre: %s Apellido: %s " % (primer_nombre, apellido))

### EJERCICIO 4
### Distintos metodos del tipo string
palabra = "El Informatorio 2020, curso Programacion"
### Encontrar la posicion donde arranca una letra o palabra
print(palabra.find("Informatorio"))
### Convertir las primeras letras de cada palabra en Mayucula
print(palabra.title())
### Transformar TODO un string a mayusculas
print(palabra.upper())
###ELIMINAR LAS ESPACIOS EXTRAS AL PRINCIPIO Y FINAL DE UN STRING
palabra2 = "    El Informatorio 2020, curso Programacion    "
print(palabra2.strip())
### Separar un string en un arreglo de Strings, CONTROLAR QUE TIPO DE VARIABLE
### ES EN CADA PASO
datos_alumno = "JUAN PEREZ, 334444777, AV. LAPRIDA 9999, 3626-1234567"
print(datos_alumno.split(","))
print(type(datos_alumno))
datos_alumno = datos_alumno.split(",")
print(type(datos_alumno))

### EJERCICIO 5
### USANDO FUNCIONES (def) CREAR UN METODO QUE NOS DEVUELVA SI UN NUMERO ES PAR O NO
def es_par(numero):
    par = False
    if numero % 2 == 0:
        par = True
    else:
        par = False
    return par

print(es_par(5))
print(es_par(8))

### EJERCICIO 6
### SE PUEDE HACER MAS CORTO QUE EL EJERCICIO 5 ???

def es_par_version2(numero):
    par = False
    if numero % 2 == 0:
        par = True
    return par

print(es_par_version2(5))
print(es_par_version2(8))

### EJERCICIO 7
### SE PUEDE HACER MAS CORTO QUE EL EJERCICIO 6 ???
def es_par_version3(numero):
    if numero % 2 == 0:
        return True
    return False

print(es_par_version3(5))
print(es_par_version3(8))

### EJERCICIO 8
### SE PUEDE HACER AUN MAS CORTO QUE EL EJERCICIO 7 ???
def es_par_version4(numero):
    return numero % 2 == 0

print(es_par_version4(5))
print(es_par_version4(8))

### EJERCICIO 8
### SE PUEDE AGREGAR OTRO FUNCION PARA IMPRIMIR UN MENSAJE PERSONALIZADO SI ES PAR O NO

def impresion_es_par(numero):
  return "Es par: " + str(numero) + " ? " + str(es_par_version4(numero))

print(impresion_es_par(5))
print(impresion_es_par(8))