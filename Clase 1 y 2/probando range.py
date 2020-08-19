numero = int(input("Ingrese un nuemro"))
cero=0
if numero >0:
    for i in range(numero):
        cero +=numero
    print(f"{numero} Al cuadrado es = {cero}")
else:
    print("Error %s ingreso \ninvalido")