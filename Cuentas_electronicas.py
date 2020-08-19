# Cuentas electronicas

## Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) 
# y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.  
# Implementa los siguientes métodos:
# 
# mostrar(): Muestra los datos de la cuenta.
# 
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    
    def __repr__(self):
        return "El Titular es: {} y la Cantidad es: {}".format(self.titular, self.cantidad)

    def mostrar(self):
        print(self.__repr__())

    def ingresar(self, cantidad):
        if cantidad < 0:
            return
        else:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        self.cantidad -= cantidad



#----------
cuentaNueva = Cuenta("Cosme Fulanito", 5000)
print(cuentaNueva)
cuentaNueva.mostrar()
cuentaNueva.ingresar(100)
cuentaNueva.mostrar()
cuentaNueva.retirar(5200)
cuentaNueva.mostrar()