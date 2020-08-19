#Este programa calcula el presupuesto de cualquier producto.
class Presupuesto:
    def __init__ (self, hojas, diseño, preparacion,tinta,otros,urgencia,transporte, packaging):
        self.hojas = hojas 
        self.diseño = diseño 
        self.preparacion = preparacion
        self.tinta = tinta
        self.otros = otros
        self.urgencia = False
        self.transporte = transporte
        self.packaging = packaging

    def __repr__(self):
        return "Cantidad de hojas: {}\nTiempo de diseño: {} min\nDemora para preparación: {} min\nPorcentaje de tinta utilizado: {} %\nOtros gastos: $ {}\nEs urgente: {}\nValor del transporte: $ {}\nPackaging: $ {}".format(self.hojas,self.diseño, self.preparacion, self.tinta, self.otros,self.urgencia, self.transporte, self.packaging)
    
    def precioHojas(self):
        tipoHoja = 0
        hojasTotales = 0

        while self.hojas >= hojasTotales:
            tipoHoja = str(input("Tipo de hoja a utilizar:\na - glossy\nb - mate\nc - adhesiva\nd - kraft\n"))
            hojasTotales = int(input("Cantidad de hojas de tipo", tipoHoja))
            print(tipoHoja)
            
            if tipoHoja == "a":
                sumaA = hojasTotales * 30
                self.hojas - hojasTotales
                print("Cantidad de hojas glossy", hojasTotales, "precio:$",sumaA)

            elif tipoHoja =="b":
                sumaB = hojasTotales * 20
                self.hojas - hojasTotales
                print("Cantidad de hojas mate", hojasTotales, "precio:$",sumaB)

            elif tipoHoja =="c":
                sumaC = hojasTotales * 60
                self.hojas - hojasTotales
                print("Cantidad de hojas adhesivas", hojasTotales, "precio:$",sumaC)

            elif tipoHoja =="d":
                sumaD = hojasTotales * 25
                self.hojas - hojasTotales
                print("Cantidad de hojas kraft", hojasTotales, "precio:$",sumaD)

            else:
                break
        valor = sumaA + sumaB + sumaC + sumaD
        print("Precio por total de hojas utilizadas: $",valor)

prueba1 = Presupuesto(5,30,39,100,0,False,200,50)
prueba1.precioHojas()