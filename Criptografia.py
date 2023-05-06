import random

characters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', ' ', '^', '%', '#', '$', '@', ',', ';', '.', ':', '¿', '?', '¡', '!', '_', '(', ')', '[', ']', '{', '}', '\\', '=', '¬', '~', 'ü', 'Ü']

def show_list():
        try:
              return characters_list
        except Exception as error:
              print(f"Ha ocurrido un error en módulo 'show_list()': {error}")
        
def prime_number(number):
        try:
            number = str(number)
            if (number.isdigit()):
                number = int(number)
                counter = 0
                for iterator in range(1,number+1):
                    if number % iterator == 0:
                        counter += 1
                return counter == 2
            else:
                print("David Torres dice: Lo siento, pero has ingresado un número no valido")
        except Exception as error:
            print(f"Ha ocurrido un error en módulo 'prime_number(number)': {error}")

def request_numbers(p,q):
        try:
            p = str(p) ; q = str(q)
            if (p.isdigit() and q.isdigit()):
                p = int(p) ; q = int(q)
                if (p >= 10) and (q >= 10):
                    if p != q:
                            if prime_number(p) and prime_number(q):
                                return p,q
                            else:
                                print("David Torres dice: Lo siento, pero los números ingresados deben ser números primos")
                                return None,None
                    else:
                            print("David Torres dice: Lo siento, pero los números ingresados deben ser diferentes")
                            return None,None
                else:
                    print("David Torres dice: Lo siento, pero debes ingresar números mayores o iguales a 10")
                    return None,None
            else:
                print("David Torres dice: Lo siento, pero debes ingresar números válidos.")
                return None,None
        except Exception as error:
            print(f"Ha ocurrido un error en módulo 'request_numbers(p,q)': {error}")

def modular_number(p,q):
      try:
        return p*q    
      except Exception as error:
        print(f"Ha ocurrido un error en módulo 'modular_number(p,q)': {error}")

def phi(p,q):
    try:
        return (p-1) * (q-1)
    except Exception as error:
        print(f"Ha ocurrido un error en módulo 'phi(p,q)': {error}")

def numbers_between(p,q):
    number_list = []
    try:
        for i in range(p,q):
             if p < i < q:
                  number_list.append(i)
        return number_list
    except Exception as error:
        print(f"Ha ocurrido un error en el módulo 'numbers_between(p,q)': {error}")

def mcd(p, q):
    try:
        while q:
            p, q = q, p % q
        return abs(p)
    except Exception as error:
        print(f"Ha ocurrido un error en el módulo 'mcd(a,b)': {error}")

def relative_prime(p,q):
    try:
        return mcd(p,q) == 1
    except Exception as error:
        print(f"Ha ocurrido un error en el módulo 'relative_prime(p,q)': {error}")

def generate_public_pass(phi_number, number_list):
    try:
        relative_prime_into_list = []
        for number_to_add in number_list:
             if relative_prime(phi_number,number_to_add):
                relative_prime_into_list.append(number_to_add)
        random_number = random.randint(0,len(relative_prime_into_list)-1)
        return relative_prime_into_list[random_number]
    except Exception as error:
        print(f"Ha ocurrido un error en módulo 'generate_public_pass(phi_number,number_list)': {error}")

def generate_private_pass(e, phi_number):
    try:
        d = 1
        while True:
             if (e * d) % phi_number == 1:
                return d
             else:
                d += 1
    except Exception as error:
        print(f"Ha ocurrido un error en el módulo 'generate_private_pass()': {error}")

def checking_characters(msg,list):

    if not isinstance(msg,str):
        print("Lo sentimos, debes ingresar un carácter que sea de tipo string")
        return False

    else:
        for element in msg:
            if not (element in list):
                print(f"Lo sentimos, se detectó un carácter que no está en la lista de carácteres válidos ({element})")
                return False
        return True

def encrypting(msg,e,n,list):
    if checking_characters(msg, list):
        encrypted_message = []

        for string in msg:

            index = list.index(string)
            index = (index**e)%n

            encrypted_message.append(index)

        return encrypted_message
    else:
        return None

def unencrypting(encrypted_list,d,n,list):
    
    original_msg = []
    msg_to_return = ""

    for string in encrypted_list:
        index = list.index(string)
        index = (index**d)%n
        original_msg.append(index)

    for values in original_msg:
        msg_to_return += original_msg[values]

    return msg_to_return




def main():
    n1 = input("Primer número (PRIMO - +2 DIGITOS): ")
    n2 = input("Segundo número (PRIMO - +2 DIGITOS): ")

    p,q = request_numbers(n1, n2)

    while None == (p or q):
        print("Números no válidos, intenta nuevamente")
        

        n1 = input("Primer número (PRIMO - +2 DIGITOS): ")
        n2 = input("Segundo número (PRIMO - +2 DIGITOS): ")
        p,q = request_numbers(n1, n2)



    number_modular = modular_number(p,q)
    phi_number = phi(p,q)
    numbers = numbers_between(1,phi_number)
    public_pass = generate_public_pass(phi_number, numbers)
    private_pass = generate_private_pass(public_pass,phi_number)


    print(f"""
    

Números válidos. Iniciando operaciones...
p = {p}
q = {q}
Clave pública = {public_pass}
    """)


    sender = input("Nombre del emisor: ")
    receiver = input("Nombre del receptor: ")


    message = input(f"{sender}, escribe un mensaje para encriptar: ")
    encrypted_message = encrypting(msg = message, e = public_pass, n = number_modular, list = characters_list)
    #unencrypted_message = unencrypting(encrypted_list = encrypted_message, d = private_pass, n = number_modular, list = characters_list)


    print(f"""
    El mensaje original fue: {message}
    El mensaje encriptado fue: {encrypted_message}
    clave privada: {private_pass}
    n: {number_modular}
    
    """)



main()

