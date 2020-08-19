class Triangulo:
    def __init__ (self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def __repr__(self):
        return "Lado 1: {}, \nLado 2: {}, \nLado 3: {}".format(self.lado1, self.lado2, self.lado3)

    def tipoDeTriangulo(self): 
        
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print ("Es un triángulo equilátero")

        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            print ("Es un triángulo escaleno")

        else:
            print ("Es un triángulo Isóceles")            

    def ladoMasLargo(self, max): #agregar los lados como parametro
        Max = max(self.lado1, self.lado2, self.lado3)
        print ("El numero más grande es: ", Max)


triangulo1 = Triangulo(10,10, 12)
print(triangulo1)
triangulo1.tipoDeTriangulo()

