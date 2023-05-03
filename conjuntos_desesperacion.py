import matplotlib.pyplot as plt
from matplotlib_venn import venn3
X = {8,10,23,37}
Y = {8,40,10,13}
Z = {8,17,10,15}

XY = X.intersection(Y)
YZ = Y.intersection(Z)
XZ = X.intersection(Z)
XYZ = (X.intersection(Y)).intersection(Z)


# Asignando configuración básica
plt.figure(facecolor = "#E2FFFE")
plt.title("Diagrama de Venn")

# Elementos de cada conjunto
UNIVERSAL = 0
A = X.difference(Y).difference(Z)
B = Y.difference(X).difference(Z)
C = Z.difference(X).difference(Y)
AB = 0
AC = 0
BC = 0
ABC = 0


print(f"""

{A}
{B}
{C}

{AB}
{AC}
{BC}
{ABC}




""")

# Asignando conjuntos a cada región y cambiando los colores
venn_diagram = venn3(
    subsets = {
        '100': A,
        '010': B,
        '001': C,
        '110': AB,
        '101': AC,
        '011': BC,
        '111': ABC
        },

        set_labels = ('A', 'B', 'C'),
        set_colors=('#FF4040', '#077FFF', '#59FF00')
    )


# Creación de recuadro para contener todos los conjuntos
Margen = plt.gca()
Margen.set_xlim(-1, 1)
Margen.set_ylim(-1, 1)
Margen.add_patch(plt.Rectangle((-1, -1), 2, 2, fill = False, linestyle = '-', linewidth = 1))

# Agregando elemento universal que no pertenece a ningún subconjunto ni región
plt.text(0.7, -0.8, f'{UNIVERSAL}', fontsize = 12, ha = 'left', va = 'top')

# Asignando nombre para identificar en la gráfica al conjunto universal
plt.text(1.12, 1, f'Universal', fontsize = 12, ha = 'left', va = 'top')

# Mostrando el diagrama de Venn


plt.show()