# # Crear un diccionario vacio
# dic = {}
# print(dic)

# # Agregar elementos
# dic["Accion"] = "Rapido y Furioso"
# print(dic)
# dic["Accion"] = "Rambo"
# print(dic)

# #Ya tiene Rambo, agregale Rapido y Furioso
# dic["Accion"] = "Rambo"
# values = dic.values()
# lista = list(values)
# lista.append("Rapido y Furioso")
# print(values)
# dic["Accion"] = lista
# print(dic)



### HASTA LAS 19:35 , REALIZAR ESTE EJERCICIO:
### EJERCICIO 1
### DEFINIR UN DICCIONARIO CON key DNI y values Nombre y Apellido
### Recorrer el diccionario
### Por cada elemento, mostrar el mensaje:
### "Bienvenido {value} tu DNI es: {key}"
### Extra: El saludo es una funcion (def holaUser)

def holaUser(x, y):
    print("Bienvenido {} tu DNI es: {}".format(y, x,))

##holaUser(3345621, "JUan Perez")

## HASTA LAS 20:05 , REALIZAMOS EL EJERCICIO
## Teniendo el diccionario anterior
## Recorrerlo
## Guardar en 3 listas, una que contenga solo dnis, otra solo
## 1er Nombre, y otra solo apellidos
## Luego imprimir cada lista
## RESULTADOS:
## lista1 ---> [123456789, 234567891]
## lista2 ---> ["Juan", "Carlos"]
## lista3 ---> ["Perez", "Acosta"]
def separarNombreYApellido(nombreCompleto):
    return nombreCompleto.split(" ")

dic2 = { 123456789: "Juan Perez", 234567891: "Carlos Acosta"}
print("Este es mi diccionario al inicio: ", dic2)

lista1 = list(dic2.keys())
print("Lista 1: ", lista1)
lista2 = []
lista3 = []
dicSalida = {}
for value in dic2.values():
    print("Valor: ", value)
    nombrePartido = separarNombreYApellido(value)
    print("Valor Separado: ", nombrePartido)
    lista2.append(nombrePartido[0])
    print(lista2)
    lista3.append(nombrePartido[1])
    print(lista3)
    dicSalida["listaDni"] = lista1
    dicSalida["listaNombre"] = lista2
    dicSalida["listaApellido"] = lista3
    print(dicSalida)
    print("Hola {} {} con DNI {}".format(dicSalida["listaNombre"][0],
     dicSalida["listaApellido"][0], dicSalida.get("listaDni")[0]))
