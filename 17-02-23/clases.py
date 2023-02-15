from math import sqrt, pi

class vehiculo():

    def __init__(self,max_vel: float,kilometer: float):
        self.max_vel: float = max_vel
        self.kilometer: float = kilometer

class punto():
    

    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
        
    def ShowCoords(self):
        print(f"El punto tiene estas coordenadas ({self.x}, {self.y})")

    def ChangeCoord(self, new_x: float, new_y: float):
        self.x = self.x + new_x
        self.y = self.y + new_y

    def CalculateDistance(self,obj2):
        distance = ((obj2.x - self.x)**2) + ((obj2.y - self.y)**2)
        distance = sqrt(distance)
        return distance


class Rectangulo():

    def __init__(self, p1: tuple, p2: tuple):
        self.p1 = p1
        self.p2 = p2

    #No entendí el ejercicio...



class Circulo():
    
    
    def __init__(self, center: object, radio: float):
        self.center: object = center
        self.radio: float = radio

    def Area(self):
        area = (self.radio) * (pi**2)
        return area

    def Perimeter(self):
        perimeter = (self.radio*2) * pi
        return perimeter

    def PointBelongs(self,point):
        formula = ((point.x - self.center)** 2) + ((point.y - self.center)** 2)
        return formula <= self.radio


class Carta():

    def __init__(self, value: float, pinta: str):
        self.value: float = value
        self.pinta: str = pinta


class CuentaBancaria():

    def __init__(self, AccountNumber: int, owner: str, balance: float):
        self.AccountNumber: int = AccountNumber
        self.owner: str = owner
        self.balance: float = balance

    def Deposit(self, amount):
        self.balance += amount

    def WithDraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Error: Saldo insuficiente...")

    def AddHandlingFee(self,percentage):
        print(f"Se aplicará (cobrará) un {percentage}% de cuota de manejo en su cuenta")
        HandlingFeeToTake = self.balance*0.2
        self.balance -= HandlingFeeToTake

    def ShowDetails(self):
        print(f"""
        Titular: {self.owner}
        Número de cuenta: {self.AccountNumber}
        Balance: {self.balance}
        Cuota de manejo: 2%
        """)