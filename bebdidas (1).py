# -*- coding: utf-8 -*-

class almacen:
    #ATRIBUTOS DE ALMACEN
    def __init__(self):
        self.listaDeProductos = []
    #METODOS DE ALMACEN
    def calcularPreciosBebidas(self):
        total = 0
        for x in self.listaDeProductos:
            total = total + x.precio
        return total
        

    def calcularPrecioDeUnaMarca(self, marca):
        total = 0
        for x in self.listaDeProductos:
            if (marca == x.marca):
                total += x.precio
        return total

    def agregarProducto(self, producto):
        for x in self.listaDeProductos:
            if (x.ide == producto.ide):
                print("Producto ya existente.")
                return
        self.listaDeProductos.append(producto)

    def eliminarProducto(self, producto):
        self.listaDeProductos.remove(producto)

    def mostrarInformacion(self):
        pass

    def __repr__(self):
        return "Lista de productos: {}".format(self.listaDeProductos)



class bebidas:
    #ATRIBUTOS DE BEBIDAS
    def __init__(self, ide, litros, precio, marca):
        self.ide = ide
        self.litros = litros
        self.precio = precio
        self.marca = marca 
    #METODOS DEL ALMACEN
    #def __repr__(self):
    #    return "IDE: {}, litros: {}, precio: {}, marca: {}".format(self.ide, self.litros, self.precio, self.marca)


class aguaMineral(bebidas):
    #ATRIBUTOS DE BEBIDAS
    def __init__(self, ide, litros, precio, marca, origen):
        bebidas.__init__(self, ide, litros, precio, marca)
        self.origen = origen
    #METODOS DEL ALMACEN
    def __repr__(self):
        return "\nIDE: {}\n litros: {}\n precio: {}\n marca: {}\n origen: {}\n \n".format(self.ide, self.litros, self.precio, self.marca, self.origen)


class gaseosa(bebidas):
    def __init__(self, ide, litros, precio, marca, azucar, promocion):
        bebidas.__init__(self, ide, litros, precio, marca)
        self.azucar = azucar
        self.promocion = promocion
    def __repr__(self):
        return "\nIDE: {}\n litros: {}\n precio: {}\n marca: {}\n azucar: {}\n promocion: {}\n \n".format(self.ide, self.litros, self.precio, self.marca, self.azucar, self.promocion)



#CODIGO PRINCIPAL
agua1 = aguaMineral(321, 2.5, 70, "agüita", "Manantial")
agua2 = aguaMineral(123, 2.5, 70, "agüita", "Manantial")
agua3 = aguaMineral(458, 2.5, 70, "agüita", "Manantial")
agua4 = aguaMineral(486, 2.5, 70, "agüita", "Manantial")
gaseosa1 = gaseosa(198, 2, 100, "cabalgata", True, "2x1")
almacen1 = almacen()
print("-"*10,"apartir de abajo se agrega dos bebidas al almacen","-"*10)
almacen1.agregarProducto(agua1)
almacen1.agregarProducto(agua2)
almacen1.agregarProducto(agua3)
almacen1.agregarProducto(agua4)
almacen1.agregarProducto(gaseosa1)
print(almacen1)
print("-"*10,"apartir de abajo se elimina el ide 321","-"*10)
almacen1.eliminarProducto(agua1)
print(almacen1)
print("-"*10,"calculamos el total de bebidas","-"*10)
total = almacen1.calcularPreciosBebidas()
print(total)
print("-"*10,"calculamos el total de bebidas de la marca agüita","-"*10)
total2 = almacen1.calcularPrecioDeUnaMarca("agüita")
print(total2)