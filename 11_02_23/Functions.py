from cmath import pi
from statistics import mean
from random import *
import time




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
    radio = input("Ingresa el rado (cm) del circulo: ")
    radio = float(radio)
    area = pi*(radio**2)
    print(f"""
===============================
¡Hey! El área del circulo en
base al radio es:

{area} cm
===============================
    """)





def Act3(max = 50):
    list = []
    for i in range(0,max):
        list.append(randint(0,max))
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
    max_list_len = int(input("¿Cuantos valores ingresaras en la lista?:"))
    list = []
    for i in range(0,max_list_len):
        new_data = float(input(f"Ingresa el valor #{i+1} de la lista: "))
        list.append(new_data)
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
        list.append(new_data)


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
            TempList.append(randint(0,90))
        matrix.append(TempList)

    print(f""""
===============================
La matrix es la siguiente:

{matrix}
===============================
    """)



def Act10():
    numero = float(input("Numero: "))
    n2 = numero
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
El factorial de {n2} es {factorial}
===============================
    """)


def Act11():
    list = []
    for i in range(1,101):
        if i%2 == 0:
            list.append(i)

    print(f"""
===============================
La lista con números pares es:
{list}
===============================
    """)


def Act12():
    for i in range(1,11):
        print(i)

def Act13():
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    print(f"""
===============================
Suma: {n1+n2}
Resta: {n1-n2}
Multiplicación: {n1*n2}
División: {n1/n2}
===============================
    """)


def Act14():
    max_list_len = int(input("¿Cuantos valores ingresaras en la lista: ?"))
    list = []
    for i in range(0,max_list_len):
        new_data = float(input(f"Ingresa el valor #{i+1} de la lista: "))
        list.append(new_data)

    result = mean(list)

    print(f"""
===============================
La media es: {result}
===============================
    """)

def Act15():
    word = input("Ingresa un texto: ")
    if word == word[::-1]:
        print(f"{word} es un palíndromo")
    else:
        print(f"{word} no es un palíndromo")

def Stopper(set = 5):
    time.sleep(set)