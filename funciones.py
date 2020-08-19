# Programa para saber que hacer con claves foráneas #

relacion1_1 = "la clave foranea puede ir en cualquiera de las dos tablas "
relacion1_N = "La clave foranea va a ir en 'muchos' "
relacionN_M = "Se crea una nueva tabla para la clave foránea "

print("-" * 70, "\n                       ¿qué es una clave foránea? \n","-" * 70,"\n Una clave foránea en una base de datos relacional \nes una clave que se usa en una tabla secundaria \ny que coincide con la clave primaria en una tabla primaria relacionada\n ")
print("*" * 70)

opc1 = input("¿quieres saber más? (Elige un número)\n          1- si | 2- no\n")
if opc1 == "1":
    print("*" * 70)
    print("Las claves foráneas pueden tener valores duplicados (multiplicidad) \nen la tabla secundaria, mientras que para las claves primarias eso no es posible. \nEl uso apropiado de claves foráneas permite exigir la integridad referencial.\n ")

opc = input("\n \n \n¿Quieres ver un ejemplo?\n \n (Elige un número)\n  1- si | 2- no\n")
if opc == "1":
    print("*" * 70)
    print("En la siguiente relación\n","*" * 70,"\n   CLIENTE ---> PRODUCTO  \n","*" * 70)
    print("\nUn cliente compra un producto el id del cliente se transformará \nen clave foránea del producto para de esta manera poder identificar que \ncliente compro ese producto.")
    print("*" * 70)
    print("\n \nEn forma de tabla, se vería así: \n \n")
    print("......._______________________________......_____________________________.......")
    print(".......|.........CLIENTE.............|......|........PRODUCTO...........|.......")
    print(".......|_____________________________|......|___________________________|.......")
    print(".......|*PK_Id : 123456..............|......|*PK_Id :654321.............|.......")
    print(".......|*Nombre: Juan Perez..........|......|*FK_cliente: 123456........|.......")
    print(".......|*Dirección: Chaco 123........|......|*Detalle: Remera Roja......|.......")
    print(".......|_____________________________|......|___________________________|.......")




elif opc == "2":
    print("Ok, continuamos...")

contin = input("Ingresa 'ok' para continuar.")
if contin == "ok":
    print("*" * 70)


print("\n \nPrueba el siguiente ejercicio: ")
print("\nLos estudiantes de la carrera de ingeniería, se inscriben a las materias del ciclo lectivo 2020.\nPara cada materia en la que un estudiante se inscriba, aparecerá una clave foránea.\n")
print("*" * 70)
print("\n \n \n \n")
print("......._______________________________......_____________________________.......")
print(".......|.........ESTUDIANTE..........|......|.........MATERIA 1.........|.......")
print(".......|_____________________________|......|___________________________|.......")
print(".......|*PK_DNI : 40775010...........|......|*PK_Id :654321.............|.......")
print(".......|*Nombre: Juan Perez..........|......|*FK_Estudiante: ????????   |.......")
print(".......|*Carrera: Ingeniería.........|......|...........................|.......")
print(".......|_____________________________|......|___________________________|.......")


respuesta1 = input("En el siguiente gráfico, ¿cuál sería la clave foránea?\nRespuestas posibles:\na: 40775010\nb: Juan Perez\nc: 654321\nEscribe la letra que corresponde a la elección: ")
if respuesta1 == "a":
    print("CORRECTO")
else: 
    print("La respuesta correcta es: 'a'")