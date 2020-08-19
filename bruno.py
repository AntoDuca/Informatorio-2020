#Creo mi clase con atributos privados
class producto:
    def __init__ (self, codigo, nombre, precio):
        self.codigo = codigo 
        self.nombre = nombre
        self.precio = precio

    def getPrecio(self):
        return self.codigo

    def precio(self, valor):
        self.__precio = valor

    #def para mostrar info de objetos
    def __str__ (self):
        return "Codigo: ", str(self.__codigo), "nombre: ", str(self.__nombre), "precio: $",float(self.__precio)

#Creacion de productos

producto1 = producto("B","Cuaderno",700)
producto2 = producto("01", "Agenda",850.50)

#para mostrar en consola

print(producto1)
print(producto1.precio())



