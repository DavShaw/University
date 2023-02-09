from Functions import *
Active = True
while(Active):
    print("\n\n¡Hola! Bienvenido al menú inicial\n\n")
    for i in range(0,14):
        print(f"{i+1}) - Ejercicio #{i+1}")

    print("911) - Salir")
    up = input("\n\nElige una opción: ")

    if up.isdigit():
        up = int(up)

        if up == 1:
            Act1()
            Stopper(3)
        elif up == 2:
            Act2()
            Stopper(3)
        elif up == 3:
            Act3()
            Stopper(3)
        elif up == 4:
            Act4()
            Stopper(3)
        elif up == 5:
            Act5()
            Stopper(3)
        elif up == 6:
            Act6()
            Stopper(3)
        elif up == 7:
            Act7()
            Stopper(3)
        elif up == 8:
            Act8()
            Stopper(3)
        elif up == 9:
            Act9()
            Stopper(3)
        elif up == 10:
            Act10()
            Stopper(3)
        elif up == 11:
            Act11()
            Stopper(3)
        elif up == 12:
            Act12()
            Stopper(3)
        elif up == 13:
            Act13()
            Stopper(3)
        elif up == 14:
            Act14()
            Stopper(3)
        elif up == 15:
            Act15()
            Stopper(3)
        elif up == 911:
            Active = False
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("¡Gracias por probar nuestro programa!")
            print("¡Nos vemos en otra ocasión!")
            print("\n\n     Errores y/o Información: jcarrillo686@soyudemedellin.edu.co\n\n")
        else:
            print("Has elegido una opción no válida...")
    else:
        print("Has ingresado algo que no es un número...")

