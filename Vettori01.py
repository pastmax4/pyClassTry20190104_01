'''
Created on 07 dic 2018

@author: mpasteri

https://docs.python.org/3/tutorial/classes.html
https://www.w3resource.com/python/python-object-classes.php
'''
import math


#--------------------------------------------------------------
#--------------------------------------------------------------
class Punto():
    #Documentazione: __doc__
    """This class is for modelling a Point in the plane."""   
    Dominio='Piano'   # class variable shared by all instances
     
    def __init__(self, X, Y ):
        self.x=X  # instance variable unique to each instance
        self.y=Y  # instance variable unique to each instance

    def DistanzaDaUnPunto(self,x0,y0):
        d = math.sqrt(math.pow((self.x-x0),2)+ math.pow((self.y-y0),2))
        return d
    
    def DistanzaDaOrigine(self):
        return self.DistanzaDaUnPunto(0,0)
        

class Segmento(Punto):
    #Documentazione: __doc__
    """This class extends Point class in the plane."""   
    
    def __init__(self,PuntoA,PuntoB):
        self.xA=PuntoA.x   
        self.yA=PuntoA.y            
        self.xB=PuntoB.x    
        self.yB=PuntoB.y
        Punto.__init__(self,self.xA,self.yA)        
        self.Lunghezza = Punto.DistanzaDaUnPunto(self, self.xB, self.yB)
        
class Triangolo():
    def __init__(self,Segmento1,Segmento2,Segmento3):
        self.Lato1=Segmento1
        self.Lato2=Segmento2
        self.Lato3=Segmento3
        self.Perimetro=self.Lato1.Lunghezza+self.Lato2.Lunghezza+self.Lato3.Lunghezza


#--------------------------------------------------------------
#--------------------------------------------------------------
class Vettore():
    
    #Documentazione: __doc__
    """This class is for modelling a vector."""    
    
    # class variable shared by all instances
    defDellaClasse='This is a vector.'
    
    # In pratica ist il costruttore della classe
    def __init__(self, pointB, pointA ):
        self.xB=pointB[0] 
        self.yB=pointB[1] 

        self.xA=pointA[0] 
        self.yA=pointA[1] 

        self.x= self.xB-self.xA
        self.y= self.yB-self.yA

        self.modulo = math.sqrt((self.x*self.x)+(self.y*self.y))
        if self.x != 0:
            self.fase = math.atan(self.y/self.x)
        else:            
            self.fase = math.pi
    
    def prodottoScalare(self,vettore2):        
        risultato = self.x * vettore2.x + self.y * vettore2.y 
        return risultato

#--------------------------------------------------------------
#--------------------------------------------------------------

A=Punto(X=2,Y=3)
print(A.Dominio)
print(A.x)
print(A.y)

print('-------------------')
B=Punto(X=8,Y=1)
print(B.Dominio)
print(B.x)
print(B.y)

print('-------------------')
C=Punto(X=6,Y=10)
print(C.Dominio)
print(C.x)
print(C.y)

print('-------------------')
S1=Segmento(PuntoA=A,PuntoB=B)
print('Segmento:',S1.xA, S1.yA,S1.xB,S1.yB)
print('Lunghezza segmento:',S1.Lunghezza)

S2=Segmento(PuntoA=B,PuntoB=C)
S3=Segmento(PuntoA=A,PuntoB=C)

print('')

Triangolo1=Triangolo(S1,S2,S3)
print('Tringolo lato1', Triangolo1.Lato1.xA, Triangolo1.Lato1.yA,Triangolo1.Lato1.xB, Triangolo1.Lato1.yB)
print('Tringolo lato2', Triangolo1.Lato2.xA, Triangolo1.Lato2.yA,Triangolo1.Lato2.xB, Triangolo1.Lato2.yB)
print('Tringolo lato2', Triangolo1.Lato3.xA, Triangolo1.Lato3.yA,Triangolo1.Lato3.xB, Triangolo1.Lato3.yB)
print('Triangolo perimetro', Triangolo1.Perimetro)




#--------------------------------------------------------------------
puntoB=[2,0]
puntoA=[0,0]

puntoD=[0,1]
puntoC=[0,0]


vet01=Vettore(pointB=puntoB,pointA=puntoA)
vet02=Vettore(pointB=puntoD,pointA=puntoC)

print('----Componenti vettore1')
print(vet01.__doc__)
print(vet01.defDellaClasse)
print(vet01.x)
print(vet01.y)

print(vet01.modulo)
print(vet01.fase)

print('----Componenti vettore2')
print(vet02.defDellaClasse)
print(vet02.x)
print(vet02.y)

print(vet02.modulo)
print(vet02.fase)


print('----prodotto scalare:')
print(vet01.prodottoScalare(vet02))


