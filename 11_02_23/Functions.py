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


def Act4():
    number = int(input("Escribe el número: "))
    if number%2 == 0:
        print(f"""
===============================
El número {number} es par
===============================
        """)
    else:
        print(f"""
===============================
El número {number} es impar
===============================
        """)



def Act5():
    deg = float(input("Ingresa los grados (En °F): "))
    Newdeg = ((deg - 32) * 5)/9
    print(f"""
===============================
La conversión de los grados de 
°F ({deg}) a °C es: {Newdeg}
===============================
    """)


def Act6():
    max_list_len = int(input("¿Cuantos valores ingresaras en la lista: ?"))
    list = []
    for i in range(0,max_list_len):
        new_data = float(input(f"Ingresa el valor #{i+1} de la lista: "))

    SumOfList = sum(list)

    print(f"""
===============================
La suma de los datos de la
lista es: {SumOfList}
===============================
    """)

def Act7():
    max_list_len = int(input("¿Cuantos valores ingresaras en la lista: ?"))
    list = []
    for i in range(0,max_list_len):
        new_data = float(input(f"Ingresa el valor #{i+1} de la lista: "))

    Max_number = max(list)
    Min_number = min(list)

    print(f"""
===============================
El mayor valor de la lista: {Max_number}
El menor valor de la lista: {Min_number}
===============================
    """)

def Act8():
    max_list_len = int(input("¿Cuantos valores ingresaras en la lista: ?"))
    list = []
    for i in range(0,max_list_len):
        new_data = input(f"Ingresa el valor #{i+1} de la lista: ")


    print(f"""
===============================
Lista original: {list}

Lista modificada: {list[::-1]}
===============================
    """)


def Act9(Len = 3):
    matrix = []
    for i in range(0,Len):
        TempList = []
        for j in range(0,Len):
            TempList.append(random.radiant(0,90))
        matrix.append(TempList)

    print(f""""
===============================
La matrix es la siguiente:

{matrix}
===============================
    """)



def Act10():
    numero = float(input("Numero: "))
    if numero <= 0:
        print(f"""
===============================
El factorial de {numero} es: 1
===============================
        """)
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    print(f"""
===============================
El factorial de {numero} es {factorial}
===============================
    """)


    