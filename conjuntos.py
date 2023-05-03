ShowVenn = input("Activar Diagrama: ")
if ShowVenn.lower() == ("t"):
    ShowVenn = True
else:
    ShowVenn = False
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

def Union(ConjuntoA: set, ConjuntoB: set):
    return ConjuntoA | ConjuntoB

def Inter(ConjuntoA: set, ConjuntoB: set):
    return ConjuntoA & ConjuntoB

def Diff(ConjuntoA: set, ConjuntoB: set):
    return ConjuntoA - ConjuntoB

def DiffSim(ConjuntoA: set, ConjuntoB: set):
    return ConjuntoA ^ ConjuntoB

def Complement(ConjuntoUniversal: set, ConjuntoA: set):
    return Diff(ConjuntoUniversal, ConjuntoA)



a = {1, 2, 3}
b = {4, 5, 6, 7}
u = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

if ShowVenn:
    import matplotlib.pyplot as plt
    from matplotlib_venn import venn3, venn3_circles,venn3_unweighted


