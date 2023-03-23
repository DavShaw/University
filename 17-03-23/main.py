#Implementación de clases y métodos del análisis del problema con Black Jack
from dataclasses import dataclass

@dataclass
class BlackJack():

    def detectar_limite():
        pass

    def doblar_apuesta():
        pass

    def restar_fichas():
        pass

    def seguir_jugando() -> bool:
        pass





@dataclass
class Jugador():

    def jugada():
        pass
    
    def pedir_carta():
        pass








@dataclass
class Mano():

    def calcular_mano():
        pass

    def comparar_mano(jugador,casa):
        pass











@dataclass
class Carta():

    pinta: str
    valor: str
    tapada: bool = False
    
    def destapar_carta(jugador):
        pass











@dataclass
class Baraja():
    
    def repartir_carta():
        pass












@dataclass
class Casa():
    pass




#Notas de clase: 
# 
# Repasar diferencias entre variable de instancia (Sé que es para crear objetos de x clase)
# y variables de clases
#
#Estudiar ClassVar y el decorador "@dataclass"
#
#No me funciona el ClassVar ¿Por qué?: Buscar en internet / Ver grabación
#
#Buscar que es ".extends" en python