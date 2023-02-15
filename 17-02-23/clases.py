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
    
    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y


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


center1 = punto(90,12)
c1 = Circulo(center1,32)
p1 = punto(901,52)



