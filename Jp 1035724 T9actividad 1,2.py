print("Ejercicio 1")

n1= int(input("ingrese el primer numero"))
n2 = int(input("ingrese el segundo numero"))
divisionReal =n1/ n2 
divEntera = n1// n2 
divModular = n1 % n2 
print(n1,"/", n2 ,"=",divisionReal)
print(n1,"//", n2 ,"=",divEntera)
print(n1,"%",n2,"=",divModular)

multiplicacion =n1*n2 
Suma= n1+n2
resta= n1-n2 

print(n1,"*",n2,"=",multiplicacion)
print(n1,"+",n2,"=",Suma)
print(n1,"-",n2,"=",resta)

igualdad= n1 == n2
diferentes =n1 != n2
mayor=n1>=n2
menor=n1<=n2

print(n1,"==",n2,"=",igualdad)
print(n1,"!",n2,"=",diferentes)
print(n1,">",n2,"=",mayor)
print(n1,"<",n2,"=",menor)

print("Ejercicio 3. jerarquia de operadores")
a=int(input("Ingrese el primer numero:"))
b=int(input("Ingrese el segundo numero:"))
c=int(input("Ingrese el tercer numero:"))

print("i", a*b+c)
print("ii",a(b+c))
print("iii",a/b+c)
print("iv", (3*a+2*b)/(c**2))


