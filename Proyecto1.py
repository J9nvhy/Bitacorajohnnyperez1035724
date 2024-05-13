#Proyecto 1
#Haydee Shirel Aquino Marroquín 1172524
#Johnny Pedro Perez Morales 1035724

#Se importa turtle
import turtle
#Definición del fondo, dibujos y textos 
def fondo():
    #Elaboración del recuadro para el cuento
    turtle.clearscreen()
    back=turtle.Turtle()
    back.teleport (-400,- 350)
    back.speed(0)
    back.forward (800)
    back.left(90)
    back.forward (700)
    back.left(90)
    back.forward(800)
    back.left(90)
    back.forward(700)
    back.back(200)
    back.left(90)
    back.forward(800)
    back.left(90)
    back.forward(450)
    back.left(90)
    back.forward(800)
    back.hideturtle()

    fondo_color=turtle.Turtle()
    fondo_color.speed(0)
    fondo_color.teleport(-400,300)
    fondo_color.color("black","LightCyan")
    fondo_color.begin_fill()
    fondo_color.forward(800) 
    fondo_color.right(90)
    fondo_color.forward(450) 
    fondo_color.right(90)
    fondo_color.forward(800) 
    fondo_color.right(90)
    fondo_color.forward(450) 
    fondo_color.right(90)
    fondo_color.end_fill()
    fondo_color.hideturtle()

def Cofre():
    #Dibujo del Cofre
    cofre=turtle.Turtle()
    cofre.speed(0)

    #Parte de abajo
    cofre.teleport(-170,40)
    cofre.color(colorsalida,colorsalida)
    cofre.begin_fill()
    cofre.left(-50)
    for i in range(3):
        cofre.forward(150)
        cofre.left(50)

    cofre.right(100)
    cofre.teleport(-170,100)
    cofre.forward(340) 
    cofre.right(90)
    cofre.forward(60) 
    cofre.right(90)
    cofre.forward(340) 
    cofre.right(90)
    cofre.forward(60) 
    cofre.right(90)

    cofre.teleport(-120,140)
    cofre.forward(240) 
    cofre.right(90)
    cofre.forward(50) 
    cofre.right(90)
    cofre.forward(240) 
    cofre.right(90)
    cofre.forward(50) 
    cofre.right(90)

    cofre.teleport(-120,40)
    cofre.circle(50) 
    cofre.teleport(120,40)
    cofre.circle(50) 
    cofre.end_fill()

    #Líneas amarillas del cofre
    cofre.color("gold","gold")
    cofre.begin_fill()

    cofre.teleport(-170,60)
    cofre.forward(340) 
    cofre.right(90)
    cofre.forward(20) 
    cofre.right(90)
    cofre.forward(340) 
    cofre.right(90)
    cofre.forward(20) 
    cofre.right(90)

    cofre.teleport(-75,40)
    cofre.forward(20) 
    cofre.left(90)
    cofre.forward(100) 
    cofre.left(90)
    cofre.forward(20) 
    cofre.left(90)
    cofre.forward(100) 
    cofre.left(90)

    cofre.teleport(55,40)
    cofre.forward(20) 
    cofre.left(90)
    cofre.forward(100) 
    cofre.left(90)
    cofre.forward(20) 
    cofre.left(90)
    cofre.forward(100) 
    cofre.left(90)

    cofre.teleport(-25,40)
    cofre.forward(50) 
    cofre.right(90)
    cofre.forward(40) 
    cofre.right(90)
    cofre.forward(50) 
    cofre.right(90)
    cofre.forward(40) 
    cofre.right(90)

    cofre.end_fill()

    #Cerradura
    cofre.color("black","black")
    cofre.begin_fill()
    cofre.teleport(0,20)
    cofre.circle(9)

    cofre.teleport(-10,10)
    for i in range(3):
        cofre.forward(20)
        cofre.left(120)
    cofre.end_fill()

    cofre.hideturtle()

def Oso():
    #Dibujo Oso de Peluche
    #Cabeza
    oso = turtle.Turtle()
    oso.speed(0)
    oso.teleport(0,100)
    oso.color(colorsalida,colorsalida)
    oso.begin_fill()
    oso.circle(50) 

    #cuerpo
    oso.teleport(-26.5,100)
    for i in range(8):
        
        oso.color()
        oso.forward(55)
        oso.right(360/8)

    #Orejas
    oso.teleport(50,170)
    oso.circle(20) 
    oso.teleport(-50,170)
    oso.circle(20) 
    oso.end_fill()

    oso.teleport(50,175)
    oso.color("antique white","antique white")
    oso.begin_fill()
    oso.circle(14) 
   
    oso.teleport(-50,175)
    oso.circle(14) 
    oso.end_fill()

    #Brazos
    oso.teleport(-80,75)
    oso.color(colorsalida,colorsalida)
    oso.begin_fill()
    for i in range(4):
        oso.forward(40) 
        oso.left(90)

    oso.teleport(45,75)
    for i in range(4):
        oso.forward(40) 
        oso.left(90)
    #Pies
    oso.teleport(-80,-50)
    for i in range(4):
        oso.forward(40) 
        oso.left(90)

    oso.teleport(45,-50)
    for i in range(4):
        oso.forward(40) 
        oso.left(90)

    #cara
    oso.teleport(0,115)
    oso.color("antique white","antique white")
    oso.begin_fill()
    oso.circle(20) 
    oso.end_fill()

    #Ojos
    oso.teleport(-20,165)
    oso.color("black","black")
    oso.begin_fill()
    for i in range(5):
        oso.forward(10)
        oso.right(360/5)

    oso.teleport(14,165)
    for i in range(5):
        oso.forward(10)
        oso.right(360/5)
    oso.end_fill()

    #Nariz
    oso.teleport(-7,145)
    oso.color("SaddleBrown","SaddleBrown")
    oso.begin_fill()
    for i in range(3):
        oso.forward(15)
        oso.right(120)
    oso.end_fill()

    oso.hideturtle()

def Barco():
    #Dibujo del barco
    #Parte de abajo
    barco=turtle.Turtle()
    barco.speed(0)

    barco.teleport(-100,20)
    barco.color("SaddleBrown","SaddleBrown")
    barco.begin_fill()
    barco.left(-45)
    for i in range(3):
        barco.forward(100)
        barco.left(45)

    #Asta
    barco.teleport(20,0)
    barco.forward(200) 
    barco.right(90)
    barco.forward(10) 
    barco.right(90)
    barco.forward(200) 
    barco.right(90)
    barco.forward(10) 
    barco.right(90)
    barco.end_fill()

    #Velas
    barco.teleport(30,60)
    barco.color(colorsalida,colorsalida)
    barco.begin_fill()
    barco.forward(140)
    barco.backward(140) 
    barco.right(90)
    barco.forward(100) 
    barco.left(125)
    barco.forward(175) 
    barco.right(35)

    barco.teleport(20,80)
    barco.forward(100) 
    barco.back(100)
    barco.left(90)
    barco.forward(80)
    barco.right(125)
    barco.forward(142)
    barco.end_fill()
    barco.right(145)

    #ventanas
    barco.color("skyblue","skyblue")
    barco.begin_fill()
    barco.teleport(-60,0)
    barco.circle(15) 
    barco.teleport(10,0)
    barco.circle(15) 
    barco.teleport(70,0)
    barco.circle(15) 
    barco.end_fill()

    #Estrella
    barco.teleport(70,120)
    barco.pencolor("gold")
    barco.pensize(3)
    for i in range(5):
        barco.forward(50)
        barco.right(144)

    barco.hideturtle()

def Doll():
    #Dibujo muñeca
    muñeca = turtle.Turtle()
    muñeca.speed(0)

    #brazos
    muñeca.teleport(-100,80)
    muñeca.color("tan","antique white")
    muñeca.begin_fill()
    muñeca.forward(200) 
    muñeca.right(90)
    muñeca.forward(30) 
    muñeca.right(90)
    muñeca.forward(200) 
    muñeca.right(90)
    muñeca.forward(30) 
    muñeca.right(90)

    #Pie izquierdo
    muñeca.teleport(-45,-30)
    muñeca.forward(30) 
    muñeca.right(90)
    muñeca.forward(60) 
    muñeca.right(90)
    muñeca.forward(30) 
    muñeca.right(90)
    muñeca.forward(60) 
    muñeca.right(90)

    #Pie derecho
    muñeca.teleport(15,-30)
    muñeca.forward(30) 
    muñeca.right(90)
    muñeca.forward(60) 
    muñeca.right(90)
    muñeca.forward(30) 
    muñeca.right(90)
    muñeca.forward(60) 
    muñeca.right(90)
    muñeca.end_fill()

    #Vestido
    muñeca.teleport(-80,-30)
    muñeca.color(colorsalida,colorsalida)
    muñeca.begin_fill()
    for i in range(3):
        muñeca.forward(160)
        muñeca.left(120)
    muñeca.end_fill()

    #Cabeza
    muñeca.teleport(0,100)
    muñeca.color("tan","antique white")
    muñeca.begin_fill()
    muñeca.circle(40) 
    muñeca.end_fill()

    #Ojos
    muñeca.teleport(-13,140)
    muñeca.color("DarkSlategray","DarkSlategray")
    muñeca.begin_fill()
    muñeca.circle(5) 
    muñeca.teleport(13,140)
    muñeca.circle(5) 
    muñeca.end_fill()

    #Estrella
    muñeca.teleport(-25,50)
    muñeca.pencolor("gold")
    muñeca.pensize(3)
    for i in range(5):
        muñeca.forward(50)
        muñeca.right(144)

    #aretes
    muñeca.teleport(40,145)
    muñeca.color("gold","gold")
    muñeca.begin_fill()
    for i in range(5):
        muñeca.forward(10)
        muñeca.right(360/5)
    muñeca.teleport(-50,145)
    for i in range(5):
        muñeca.forward(10)
        muñeca.right(360/5)
    muñeca.end_fill()
    #moño derecho
    muñeca.teleport(1,178)
    muñeca.color(colorsalida,colorsalida)
    muñeca.begin_fill()
    muñeca.left(30) 
    muñeca.forward(30) 
    muñeca.right(120) 
    muñeca.forward(30)
    muñeca.right(120) 
    muñeca.forward(30) 

    #Moño izquierdo
    muñeca.teleport(1,178)
    muñeca.right(10) 
    muñeca.forward(30) 
    muñeca.left(120) 
    muñeca.forward(30)
    muñeca.left(120) 
    muñeca.forward(30) 
    muñeca.end_fill()

    muñeca.hideturtle()
    
def Carro():
    #Dibujo del carro
    carro=turtle.Turtle()
    carro.speed(0)
    #Parte de abajo
    carro.teleport(40,120)
    carro.color(colorsalida,colorsalida)
    carro.begin_fill()
    carro.forward(300) 
    carro.right(90)
    carro.forward(75) 
    carro.right(90)
    carro.forward(300) 
    carro.right(90)
    carro.forward(75) 
    carro.right(90)
    carro.end_fill()

    carro.teleport(40,100)
    carro.color("gold","gold")
    carro.begin_fill()
    for i in range(4):
        carro.forward(20) 
        carro.left(90)
    carro.end_fill()

    #llantas
    carro.teleport(110,0)
    carro.color("black","black")
    carro.begin_fill()
    carro.circle(35)
    carro.teleport(280,0) 
    carro.circle(35)
    carro.end_fill()

    carro.teleport(110,13)
    carro.color("Darkgray","Darkgray")
    carro.begin_fill()
    carro.circle(20)
    carro.teleport(280,13) 
    carro.circle(20)
    carro.end_fill()

    #Parte de arriba
    carro.teleport(300,120)
    carro.color(colorsalida,colorsalida)
    carro.begin_fill()
    carro.left(135)
    for i in range(3):
        carro.forward(80)
        carro.left(45)
    carro.end_fill()

    carro.teleport(275,120)
    carro.color("skyblue","skyblue")
    carro.begin_fill()
    carro.left(225)
    for i in range(3):
        carro.forward(60)
        carro.left(45)
    carro.end_fill()

    carro.teleport(230,175)
    carro.color(colorsalida,colorsalida)
    carro.begin_fill()
    carro.forward(55) 
    carro.right(90)
    carro.forward(10) 
    carro.right(90)
    carro.forward(55) 
    carro.right(90)
    carro.forward(10) 
    carro.right(90)
    carro.end_fill()

    carro.hideturtle()

#dibujo de bloques
    bloque=turtle.Turtle()
    bloque.speed(0)
    #cuadrado
    bloque.teleport(-150,20)
    bloque.color("coral","coral")
    bloque.begin_fill()
    for i in range(4):
        bloque.forward(60) 
        bloque.left(90)
    bloque.end_fill()

    #rectángulo de abajo
    bloque.teleport(-305,20)
    bloque.color(colorsalida,colorsalida)
    bloque.begin_fill()
    bloque.forward(150) 
    bloque.left(90)
    bloque.forward(60) 
    bloque.left(90)
    bloque.forward(150) 
    bloque.left(90)
    bloque.forward(60) 
    bloque.left(90)
    bloque.end_fill()

    #rectángulo de arriba
    bloque.teleport(-270,80)
    bloque.color("blueviolet","blueviolet")
    bloque.begin_fill()
    bloque.forward(150) 
    bloque.left(90)
    bloque.forward(60) 
    bloque.left(90)
    bloque.forward(150) 
    bloque.left(90)
    bloque.forward(60) 
    bloque.left(90)
    bloque.end_fill()

    #triángulo
    bloque.teleport(-230,140)
    bloque.color("green","green")
    bloque.begin_fill()
    for i in range(3):
        bloque.forward(80)
        bloque.left(120)
    bloque.end_fill()   
    
def Texto1():
    #Texto: Escena No.1
    texto1=turtle.Turtle()
    texto1.speed(0)
    style = ('Aptos', 14)

    texto1.teleport(0,325)
    texto1.write("Los Tesoros",False,"center",("Aptos",14,"bold"))
    texto1.teleport(0,305)
    texto1.write("Escena 1: El Descubrimiento",False,"center",style)
    texto1.teleport(0,-200)
    texto1.write(f"En un pequeño pueblo rodeado de bosques frondosos vivía {nombre},",False,"center",style) 
    texto1.teleport(0,-225)
    texto1.write(f"un niño de {edad} años . Era curioso y lleno de energía. Un día, mientras",False,"center",style)
    texto1.teleport(0,-250)
    texto1.write("exploraba el desván de su casa, descubrió un cofre polvoriento escondido",False,"center",style)
    texto1.teleport(0,-275)
    texto1.write("detrás de viejas mantas. Con asombro, abrió el cofre y encontró cinco tesoros",False,"center",style)
    texto1.teleport(0,-300)
    texto1.write("esperando ser descubiertos.",False,"center",style)
    texto1.hideturtle()
    
def Texto2():
    #Texto: Escena No.2
    texto2=turtle.Turtle()
    texto2.speed(0)
    style = ('Aptos', 14)

    texto2.teleport(0,325)
    texto2.write("Los Tesoros",False,"center",("Aptos",14,"bold"))
    texto2.teleport(0,305)
    texto2.write("Escena 2: El Primer Tesoro",False,"center",style)
    texto2.teleport(0,-225)
    texto2.write(f"Dentro del cofre, {nombre} encontró un oso de peluche desgastado pero",False,"center",style) 
    texto2.teleport(0,-250)
    texto2.write("amorosamente cuidado. Este oso había sido el compañero de juegos de su",False,"center",style)
    texto2.teleport(0,-275)
    texto2.write(f"madre cuando era niña. {nombre} decidió que este oso sería su confidente en",False,"center",style)
    texto2.teleport(0,-300)
    texto2.write("todas sus aventuras. Juntos, explorarían el mundo desde su habitación.",False,"center",style)
 
    texto2.hideturtle()

def Texto3():
    #Texto: Escena No.3
    texto3=turtle.Turtle()
    texto3.speed(0)
    style = ('Aptos', 14)

    texto3.teleport(0,325)
    texto3.write("Los Tesoros",False,"center",("Aptos",14,"bold"))
    texto3.teleport(0,305)
    texto3.write("Escena 3: El Segundo Tesoro",False,"center",style)
    texto3.teleport(0,-200)
    texto3.write(f"Entre los recuerdos guardados, {nombre} halló un pequeño barco de madera",False,"center",style) 
    texto3.teleport(0,-225)
    texto3.write("tallado a mano. Este barco había sido el tesoro más preciado de su abuelo",False,"center",style)
    texto3.teleport(0,-250)
    texto3.write(f"cuando era joven. {nombre} decidió que llevaría este barco en todas sus ",False,"center",style)
    texto3.teleport(0,-275)
    texto3.write("expediciones imaginarias por los mares desconocidos de su habitación,",False,"center",style)
    texto3.teleport(0,-300)
    texto3.write("soñando con ser un intrépido capitán.",False,"center",style)

    texto3.hideturtle()

def Texto4():
    #Texto: Escena No.4
    texto4=turtle.Turtle()
    texto4.speed(0)
    style = ('Aptos', 14)

    texto4.teleport(0,325)
    texto4.write("Los Tesoros",False,"center",("Aptos",14,"bold"))
    texto4.teleport(0,305)
    texto4.write("Escena 4: El Tercer Tesoro",False,"center",style)
    texto4.teleport(0,-200)
    texto4.write(f"Al fondo del cofre, {nombre} encontró una muñeca de porcelana ",False,"center",style) 
    texto4.teleport(0,-225)
    texto4.write("delicadamente vestida. Esta muñeca había pertenecido a su tía abuela y ",False,"center",style)
    texto4.teleport(0,-250)
    texto4.write("había sido guardada con gran cuidado. Aunque al principio dudaba en jugar ",False,"center",style)
    texto4.teleport(0,-275)
    texto4.write(f"con ella, {nombre} pronto descubrió que la muñeca era una gran compañera ",False,"center",style)
    texto4.teleport(0,-300)
    texto4.write("en sus juegos de imaginación, creando historias y aventuras juntos.",False,"center",style)

    texto4.hideturtle()

def Texto5():
    #Texto: Escena No.5
    texto5=turtle.Turtle()
    texto5.speed(0)
    style = ('Aptos', 14)

    texto5.teleport(0,325)
    texto5.write("Los Tesoros",False,"center",("Aptos",14,"bold"))
    texto5.teleport(0,305)
    texto5.write("Escena 5: El Cuarto y Quinto Tesoro ",False,"center",style)
    texto5.teleport(0,-190)
    texto5.write("Entre los últimos objetos encontrados estaban un conjunto de bloques de ",False,"center",style) 
    texto5.teleport(0,-215)
    texto5.write("construcción coloridos y un pequeño carrito de carreras. Estos juguetes ",False,"center",style)
    texto5.teleport(0,-240)
    texto5.write("habían sido los favoritos de su padre cuando era niño. Con los bloques ",False,"center",style)
    texto5.teleport(0,-265)
    texto5.write(f"{nombre} construía ciudades imaginarias y castillos impresionantes. Con el ",False,"center",style)
    texto5.teleport(0,-290)
    texto5.write("carrito organizaba emocionantes carreras por los pasillos de su hogar, ",False,"center",style)
    texto5.teleport(0,-315)
    texto5.write("dejando volar su creatividad y energía. Fin.",False,"center",style)

    texto5.hideturtle()

#Nombre del cuento
print("Cuento: Los Tesoros")
print("")
#Entrada de datos
nombre=input("Ingrese su nombre: ")
edad=input("Ingrese su edad: ")
print("")

#Creación de ventana de Turtle
turtle.setup(width=800, height=750)
turtle.Screen().title("Proyecto No.1")

#Mantener la ventana de Turtle abierta durante la ejecución
turtle.Screen().tracer(0)
#"tracer" para desactivar actualizaciones automáticas
turtle.hideturtle()

#Ciclo 
while True:
    print("Elija un color:")
    print("1. Rojo","2. Azul ", "3. Rosado ", "4. Verde","5. Anaranjado","6. Salir", sep="\n")
    color=int(input("Ingrese el número de su opción:"))
    print("")
    if color == 6:
        print("FIN")
        break  # Salir del bucle si el usuario elige "Salir"

    if color<1 or color>5:
        print("Error: Ingrese un color dentro del rango")
        continue  # Volver al inicio del bucle para pedir una nueva entrada de usuario

    print("Elija una escena:")
    print("1. Escena 1","2. Escena 2", "3. Escena 3", "4. Escena 4","5. Escena 5", sep="\n")
    escena=int(input("Ingrese el número de su opción:"))
    print("")

    if escena<1 or escena>5:
        print("Error: Ingrese una escena dentro del rango")
        continue  # Volver al inicio del bucle para pedir una nueva entrada de usuario
    else:
        colorsalida = ""
        match color:
            case 1:
                colorsalida = "darkred"
            case 2:
                colorsalida = "steelblue"
            case 3:
                colorsalida = "orchid"
            case 4:
                colorsalida = "forestgreen"
            case 5:
                colorsalida = "chocolate"
        fondo()
        match escena:
            case 1:
                Texto1()
                Cofre()
                
            case 2:
                Texto2()
                Oso()
                
            case 3:
                Texto3()
                Barco()
                
            case 4:
                Texto4()
                Doll()
                
            case 5:
                Texto5()
                Carro()
#Salir del programa
turtle.done()