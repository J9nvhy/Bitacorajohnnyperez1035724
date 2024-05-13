print("semana no.01: Ejerciciio 1")

n = int(input("ingrese un numero a 0"))
#Declaracion de variables
a = 0
b = 1 
c = 0
i = 2
resultado= ""

if (n>0):
    resultado=  str (a)

    if(n>1):
        resultado += "," + str (b)
    while(i<n):
        c = a + b 
        resultado += "," + str(c) 
        a = b
        b = c
        i = i + 1
    print(resultado)
else:
    print(resultado)    



print("Semana No .11: Ejercicio 2")
n = int(input(" Ingrese un numero mayor 0"))

if(n<= 0):
    print(" Error: el numero debe ser mayor a cero")

resultadoA= 0 
for x in range (1, n+1):
    resultadoA += (1/x)
print("Inciso A:", resultadoA)

# smenana no 11 ejercicio 3




x = int(input("ingrese un numero: "))
a = int(input("ingrese otro numero: "))
n = int(input("ingrese el numero final: "))

factorialn= 1
for i in range(1,n + 1):
    factorialn *= i

suma = 0
for k in  range(n +1):
    coeficientebinomial = 1
    for i in range( 1, k + 1):
        coeficientebinomial *= (n - i + 1) // i


    suma += (x ** k) * (a **( n - k)) / coeficientebinomial

print(" El resultado de la suma es:",suma)




            