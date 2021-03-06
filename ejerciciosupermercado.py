from os import system  #esto es para que
system("cls")        #limpie la consola

class supermercado:
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.catalogo = list()
        self.__producto = None
        self.__precio = 0

    def __repr__(self):
        return "{}".format(self.catalogo)
    
    def agregarProducto(self, marca, tipo, precio, precioCuidado = False, primeraNecesidad = False):
        self.__producto = producto(marca, tipo, precio, precioCuidado, primeraNecesidad)
        self.catalogo.append(self.__producto)
        self.__producto = None

    def cantidadTotalProductos(self):
        print("Cantidad total de productos: ",len(self.catalogo))

    def precioTotalProductos(self):
        for x in self.catalogo:
            self.__precio = self.__precio + x.precio
        print("Precio total de productos: ",self.__precio)

class producto:
    def __init__(self, marca, tipo, precio, precioCuidado = False, primeraNecesidad = False):
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.precioCuidado = precioCuidado
        self.primeraNecesidad = primeraNecesidad

    def __repr__(self):
        return "\nMarca: {}\nTipo: {}\nPrecio: {}\nPrecioCuidado: {}\nPrimera necesidad: {}\n".format(self.marca, self.tipo,self.precio, self.precioCuidado, self.primeraNecesidad)

#CODIGO PRINCIPAL

supermercado1 = supermercado('Carrefour','Av. San Martin 446')
supermercado1.agregarProducto('Serenisima', 'Leche',70,True,True)
supermercado1.agregarProducto('Sancor', 'Yogur',90,True,True)
supermercado1.agregarProducto('Coca Cola', 'Gaseosa',120)
supermercado1.agregarProducto('Pepsi', 'Gaseosa',130)
supermercado1.agregarProducto('Paladini', 'Salchicha',35)
supermercado1.agregarProducto('Blanca Flor', 'Harina',45,True,True)
supermercado1.agregarProducto('Ace', 'Azucar',60)
supermercado1.agregarProducto('Ala', "Jabon en Polvo",40)
print(supermercado1)
supermercado1.cantidadTotalProductos()
supermercado1.precioTotalProductos()






"""producto1 = producto('Coca Cola', 'Gaseosa', 120)
print(producto1)
producto2= producto('Serenisima', 'Leche',70,True,True)
print(producto2)"""