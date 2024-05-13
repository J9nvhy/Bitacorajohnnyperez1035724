print("Semana No. 10: Ejercicio 1")
mesEntrada= int(input("Ingrese un numero del 1-12"))
mesSalida= ""
match mesEntrada: 
    case 1: 
        mesSalida= "Enero"
    case 2:
        mesSalida= "febrero"
    case 3: 
        mesSalida= "Marzo"
    case 4: 
        mesSalida= "abril"
    case 5: 
        mesSalida= "Mayo"
    case 6:
        mesSalida= "Junio"
    case 7: 
        mesSalida= "Julio"
    case 8: 
        mesSalida= "Agosto"
    case 9: 
        mesSalida= "Septiembre"
    case 10:
        mesSalida= "Octubre"
    case 11: 
        mesSalida= "Novimbre"
    case 12:
        mesSalida="Diciembre"
    case _ :
        ("Error: El numero a ingresar debe estar contenido entre 1")

print(f"MES: {mesSalida}")

            