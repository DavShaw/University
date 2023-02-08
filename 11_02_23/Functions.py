from cmath import pi 

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

