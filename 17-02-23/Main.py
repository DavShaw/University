from clases import *
#Si ve que en consola no se muestra nada respecto a ciertos métodos de X clase
#esto se puede deber a que varios métodos retornan valor, mas no lo imprimen

Carrito = vehiculo(210,25)


Puntito1 = punto(25,5)
Puntito2 = punto(12,52)

Puntito1.CalculateDistance(Puntito2)
Puntito1.ChangeCoord(12,52)
Puntito1.ShowCoords()


Circulito = Circulo(Puntito1,25)

Circulito.Area()
Circulito.Perimeter()
Circulito.PointBelongs(Puntito1,Puntito2)


Cuentita = CuentaBancaria(9521,"David Torres",9025)

Cuentita.Deposit(25)
Cuentita.WithDraw(12)
Cuentita.AddHandlingFee(2)
Cuentita.ShowDetails()


Carta1 = Carta(1,"pintA1")