from random import shuffle

class carta:
    def __init__ (self, figura, valor):
        self.figura = figura
        self.valor = valor

    def __repr__ (self):
        return "{} de {}".format(self.figura, self.valor)

class Baraja:
    def __init__(self):
        figuras = ['Espadas', 'Copas', 'Bastos', 'Oros']
        valores = ['1', '2', '3', '4', '5', '6', '7', 'Sota', 'Caballo', 'Rey']
        self.cartas = [carta(figura, valor) for figura in figuras for valor in valores]
        self.descarte = list()

    def __repr__(self):
        return "Cartas: {}".format(self.cartas)

    def barajar(self):
        return shuffle(self.cartas)

    def siguienteCarta(self):
        if (len(self.cartas) == 0):
            raise ValueError('Todas las cartas se repartieron')
        cartaRepartida = self.cartas.pop() 
        self.descarte.append(cartaRepartida) 
        print(cartaRepartida)

    def cartasDisponibles(self):
        return len(self.cartas)

    def darCartas(self, cantidad):
        if (self.cartasDisponibles() < cantidad):
            raise ValueError('No hay cartas')
        print('Estas son sus', cantidad,"cartas")
        for _ in range(cantidad):
            print(self.siguienteCarta())

    def cartasMonton(self):
        if (self.descarte == 0):
            print('Todavía no')
        return descarte(self)

    def mostrarBaraja(self):
        pass






#Espacio objetos
print("*"*8,"Bienvenido al barajador de cartas","*"*8)
carta1 = carta("1", "Espadas")
print(carta1)
baraja1 = Baraja()
