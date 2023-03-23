from dataclasses import dataclass


@dataclass
class Elemento():
    nombre: str
    def __eq__(self, other: object) -> bool:
        return self == other



class Conjunto():

    contador: int = 0
    __id: int
    
    def __init__(self, nombre):

        self.elementos = []
        self.nombre = nombre

        self.contador += 1
        self.__id = self.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, element: Elemento) -> bool:
        return element in self.elementos


    def agregar_elemento(self, element: Elemento) -> None:

        if not (self.contiene(self, element)):
            self.elementos.append(element)

    def unir(self, conjunto: object) -> None:
        for elementos_conjunto in conjunto.elementos:
            if not (self.contiene(elementos_conjunto)):
                self.elementos.append(elementos_conjunto)

    def __add__(self, otro_conjunto):
        n_conjunto = Conjunto(self.nombre)
        n_conjunto.elementos = self.elementos
        n_conjunto.unir(otro_conjunto)
        return n_conjunto

    def intersectar(self, conjunto):
        n_conjunto = Conjunto(self.nombre)

        for repited_elements in conjunto.element:
            if repited_elements in self.elementos[repited_elements]:
                n_conjunto.elementos.append(repited_elements)
        #Acá se pudo usar un List Comphre...algo, pero queda demasiado largo e imposible de leer
        return n_conjunto

    def __str__(self):
        string_repre = ""

        for i in self.elementos:
            string_repre += self.elementos.nombre
            string_repre += ", "
        return string_repre



    


