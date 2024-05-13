print("Semana No.12: Ejercicio 1")
print("a. Sumatoria","b. Factorial", "c. Tablas de Multiplicar", "d. Número perfecto", sep="\n")

opcion=input("Ingrese la letra de su opción:")

match opcion:
    case "a":
        n= int(input("Ingrese un número entero positivo:"))

        if (n>0):
            sumatoria=0
            i = 1
            while (i <= n):
                sumatoria=sumatoria + i
                i = i + 1
            print("Sumatoria es:", sumatoria)
        else:
            print("Error: El número debe ser mayor a cero")
    case "b":
        n=int(input("Ingrese un número entero positivo:"))
        
            
    case "c":
        titulocolumna="\t"

        for i in range(1,11):
            titulocolumna = titulocolumna + str(i) + "\t"
        print(titulocolumna)

        for filas in range(1,11):
            cadenafila= str(filas) +"\t"
            for columnas in range (1,11):
                cadenafila= cadenafila + str(filas*columnas)+"\t"
            print(cadenafila)
        
    case "d":
        numero = int(input("Ingrese un número entero positivo: "))

if numero <= 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == numero:
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")