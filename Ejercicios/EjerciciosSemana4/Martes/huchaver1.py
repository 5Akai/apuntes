hucha = {'50' : 0, '100' : 0, '200' : 0, '500' : 0, '1000' : 0}
total_dinero = 0

while True:

    accion = input("Quieres insertar o romper? ").lower()
    finalizar = "no"

    if accion == "insertar":
        bill50 = int(input("Cuantos billetes de 50 quieres insertar? "))
        bill100 = int(input("Cuantos billetes de 100 quieres insertar? "))
        bill200 = int(input("Cuantos billetes de 200 quieres insertar? "))
        bill500 = int(input("Cuantos billetes de 500 quieres insertar? "))
        bill1000 = int(input("Cuantos billetes de 1000 quieres insertar? "))

        hucha['50'] = hucha['50'] + bill50
        hucha['100'] = hucha['100'] + bill100
        hucha['200'] = hucha['200'] + bill200
        hucha['500'] = hucha['500'] + bill500
        hucha['1000'] = hucha['1000'] + bill1000
    elif accion == "romper":
        for clave, valor in hucha.items():
            total_dinero += int(clave) * valor
            print("Billetes de " + clave + " es " + str(valor))

        print("")
        print("El total de dinero es:", total_dinero)
        finalizar = True 
        finalizar = "si"


    if finalizar == "si":
        break