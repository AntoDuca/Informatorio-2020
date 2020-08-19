"""Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones 
por cantidad según el siguiente criterio:

 i.      a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.

El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. 
Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y la cantidad total pedida 
por el mismo, determinar el importe bruto bonificado.
"""
def registrarTipoCliente():
   while True:
       try:
           tipoCliente = str(input("Ingrese el tipo de cliente.\n[L] - Libreria\n[P] - Particular\n"))
           if tipoCliente not in ["L", "P"]:
               raise ValueError("Debe ingresar un valor valido")
       except Exception as e:
           print("Ha ocurrido un error =>", type(e).__name__)
       else:
           break
   return tipoCliente
 
def registrarImporte():
   while True:
       try:
           importe = float(input("Ingrese el importe de la compra:\n"))
       except Exception as e:
           print("Ha ocurrido un error =>", type(e).__name__)
       else:
           break
   return importe
 
def registrarCantidadCompra():
   while True:
       try:
           cantidad = int(input("Ingrese la cantidad de libros comprados:\n"))
       except Exception as e:
           print("Ha ocurrido un error =>", type(e).__name__)
       else:
           break
   return cantidad

def bonificacion(cliente, cantidad, importe):
    if cliente == "L":
        if cantidad > 24:
            importe = importe - (importe * 0.25) 
        else:
            importe = importe - (importe * 0.20)
    else:
        if cantidad >= 18:
            importe = importe - (importe * 0.10) 
        elif cantidad >= 6 and cantidad <= 18:
            importe = importe - (importe * 0.05)
    return importe



tipoCliente = registrarTipoCliente()
importe = registrarImporte()
cantidad = registrarCantidadCompra()
descuento = bonificacion(tipoCliente ,cantidad, importe)
 


print("Chau!!", tipoCliente, " con importe: ", importe, " llevaste : ", cantidad, " libros y descuento", descuento)