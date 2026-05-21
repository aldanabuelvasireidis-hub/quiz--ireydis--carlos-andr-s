"""
Esta función nos muestra el funcionamiento del sistema de luz, aire y puerta automatica de un supermercado
"""
personas = 0
abierto = True

dia = input("Ingrese el dia: ")
hora = int(input("Ingrese la hora: "))
if dia == "Lunes" or "Martes" or "Miercoles" or "Jueves" or "viernes" or "Sabado" or "Domingo":

    if hora >= 7:

        print("Supermercado abierto")
        print("Luces encendidas")
        print("Aire encendido")

    else:

        print("Supermercado cerrado")
        abierto = False

else:

    if hora <= 20:

        print("Supermercado cerrado")
        abierto = False

while abierto == True:

    personas = int(input("Ingrese cantidad de personas: "))

    if personas > 0:

        print("Puerta automatica abierta")

    else:

        print("Puerta automatica cerrada")

    salir = input("Desea terminar la jornada? ")

    if salir == "si":

        personas = int(input("Cuantas personas quedan dentro?: "))

        if personas == 0:

            print("Luces apagadas")
            print("Aire apagado")
            print("Puertas bloqueadas")
            print("Fin de jornada")

            abierto = False

        else:

            print("Todavia hay personas dentro")