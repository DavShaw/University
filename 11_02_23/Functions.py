from cmath import pi
from random import random,randint




def Act1():
    user_name = input("¿Cuál es tu nombre?: ")
    user_age = input("¿Cuál es tu edad?: ")
    print(f"""
===============================
¡Hola! Hemos recolectado tu info

Te llamas: {user_name}
Tu edad es: {user_age}
===============================
    """)
    return None





def Act2():
    radio = input("Ingresa el rado del circulo: ")
    radio = float(radio)
    area = pi*(radio**2)
    print(f"""
===============================
¡Hey! El área del circulo en
base al radio es:

{area}
===============================
    """)





def Act3(max = 50):
    list = []
    for i in range(0,max):
        list.append(random.radian(0,max))
    print(f"""
===============================
¡Hola! Acá está la lista de
los números random:

{list}
===============================
    """)


