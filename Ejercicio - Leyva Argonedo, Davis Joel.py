#Ejercicio propuesto en clase
from math import sqrt
class Punto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x},{self.y})" 

    def cuadrante(self):
        if self.x==0 and self.y!=0:
            print(f"{self} se sitúa sobre el eje de las ordenadas (eje Y)")
        elif self.x!=0 and self.y==0:
            print(f"{self} se sitúa sobre el eje de las abcisas (eje X)")
        elif self.x==0 and self.y==0:
            print(f"{self} se sitúa sobre el origen de coordenadas")
        elif self.x>0 and self.y>0:
            print(f"{self} se sitúa en el primer cuadrante")
        elif self.x<0 and self.y>0:
            print(f"{self} se sitúa en el segundo cuadrante")
        elif self.x<0 and self.y<0:
            print(f"{self} se sitúa en el tercer cuadrante")
        elif self.x>0 and self.y<0:
            print(f"{self} se sitúa en el cuarto cuadrante")

    def vector(self,p):
        a=p.x-self.x
        b=p.y-self.y
        return f"El vector resultante es ({a},{b})"

    def distancia(self,point1):
        return f"La distancia es: {sqrt((point1.x-self.x)**2+(point1.y-self.y)**2)}"

print("Escribir las coordenadas del primer punto")

a=int(input("Digitar la coordenada en X: "))
b=int(input("Digitar la coordenada en Y: "))
print()
print("Escribir las coordenadas del segundo punto")
c=int(input("Digitar la coordenada en X: "))
d=int(input("Digitar la coordenada en Y: "))
print()
print("LOS RESULTADOS SON LOS SIGUIENTES")
punto1=Punto(a,b)
punto2=Punto(c,d)

punto1.cuadrante()
print(punto1.vector(punto2))
print(punto1.distancia(punto2))