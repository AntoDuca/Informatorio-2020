 # -*- coding: utf-8 -*-

 #Falta terminar la funcion MOSTRAR LIBROS POR CALIFICACION

from os import system  #esto es para que
system("clear")        #limpie la consola

class Libro:
    def __init__(self, titulo, autor, nro_paginas, calificacion):
        self.titulo = titulo
        self.autor = autor
        self.nro_paginas = nro_paginas

        if calificacion in range(0,11):
            self.calificacion = calificacion
        else:
            print("no está en el rango")
    
    def __repr__(self):
        return "Titulo: {}\nAutor: {}\n".format(self.titulo,self.autor)

    def getCalificacion(self, calificacion):
        return self.calificacion
    
    def setCalificacion(self, calificacion):
        self.calificacion = calificacion

class conjuntoLibros:
    def __init__(self, nombreConjunto):
        self.nombreConjunto = nombreConjunto
        self.listaDeLibros = list() #creamos una lista vacía para cargar libros

    def getNombreConjuntoLibros(self):
        return self.nombreConjunto

    def setNombreConjuntosLibros(self, nombre):
        self.nombreConjunto = nombre

    def getListaDeLibros(self):
        return self.listaDeLibros

    def __repr__(self):
        return "Nombre: {}\n Lista de libros: {}\n".format(self.nombreConjunto,self.listaDeLibros)

    def añadirLibro(self, listaDeLibros):
        cond = True
        while cond == True:
            dato = str(input("¿Hay espacio disponible?\n S/N \n"))
            if (dato == "S") or (dato == "s"):#ver metodo mayus/minus
                self.listaDeLibros.append(Libro)
                cond = False
            elif (dato == "N") or (dato == "n"):
                print("No hay espacio disponible")
                cond = False
            else:
                print("Ingrese datos validos")

    def __eliminarLibros_porTitulo(self, titulo):
        for x in self.listaDeLibros: #para el elemento x en la lista de libros
            if (titulo == x.titulo): #si el titulo es igual al titulo del emento x
                self.listaDeLibros.remove(x) #remover ese elemento x de la lista
        print("Libros por titulos eliminados")

    def __eliminarLibros_porAutor(self, autor):
        for x in self.listaDeLibros:
            if (autor == x.autor):
                self.listaDeLibros.remove(x)
        print("Libros por autor eliminados")

    def eliminarLibro(self):
        cond = True
        while cond == True:
            dato = (input("Desea eliminar libro por \nA - Titulo \nB - Autor\n"))
            if dato == "A":
                dato = input("Ingrese un Título de libro:\n")
                self.__eliminarLibros_porTitulo(dato)
            elif dato == "B":
                dato = input("Ingrese un Autor de libro:\n")
                self.__eliminarLibros_porAutor(dato)
            else:   
                print("Error")
            dato = input("¿Desea continuar eliminando?\n S/N: ")
            cond2 = True
            while cond2 == True:
                if (dato == "N") or (dato == "n"):
                    cond = False
                    cond2 = False
                elif (dato == "S") or (dato == "s"):
                    cond2 = False
                else:
                    print("Opcion inexistente")




#ESPACIO DE FUNCIONES
def crearLibro(titulo, autor, nro_paginas, calificacion):
    libro = Libro(titulo, autor, nro_paginas, calificacion)
    return libro


def menu():
    cond = True
    while cond == True:
        system('clear') #esto es para que limpie la consola
        conjunto = conjuntoLibros("Mis libros favoritos")
        print("*"*25,"MIS LIBROS FAVS")
        print("1 - Ver mis libros favoritos")
        print("2 - Añadir libro nuevo")
        print("3 - Eliminar libros")
        print("4 - Mostrar libros por calificacion")
        print("5 - Salir")
        dato = int(input("Ingrese opcion: "))
        if (dato == 1):
            system("clear")
            print("*"*25,"Mis libros favoritos")
            print(conjunto)
            opcion = input("Presione enter para volver al menú.")
            if (opcion == '\n'):
                system("clear")
        elif (dato == 2):
            system("clear")
            print("*"*25,"Añadir libro")
            titulo = input("Ingrese el titulo: ")
            autor = input("Ingrese el nombre del autor: ")
            nro_paginas = int(input("Ingrese numero de paginas: "))
            calificacion = int(input("Ingrese calificación: "))
            conjunto.añadirLibro(crearLibro(titulo,autor,nro_paginas,calificacion))
        elif (dato == 3):
            system("clear")
            print("*"*25,"Eliminar libro")
            conjunto.eliminarLibro()
        elif (dato == 4):
            pass
        elif (dato == 5):
            cond = False

    

#ESPACIO DE CODIGO PRINCIPAL

menu()

libro1 = Libro("cien años de soledad", "Garcia Marquez", "300", 9)
conjunto = conjuntoLibros()

print(libro1)
print(conjunto)

conjunto.agregarLibro(libro1)

print(conjunto)

conjunto.eliminarLibro()

print(conjunto)
