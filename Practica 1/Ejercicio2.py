import math
class EcuacionLineal:
    def __init__(self,a,b,c):
        self.__a=a
        self.__b=b
        self.__c=c
    def getDiscriminante(self):
        return (self.__b*self.__b)-(4*self.__a*self.__c)
    def getRaiz1(self):
        if(self.getDiscriminante()>=0):
            r1=(-self.__b+math.sqrt(self.getDiscriminante()))/(2*self.__a)
            return r1
        return "Error"
    def getRaiz2(self):
        if(self.getDiscriminante()>=0):
            r2=(-self.__b-math.sqrt(self.getDiscriminante()))/(2*self.__a)
            return r2
        return "Error"
    def __str__(self):
        return "Ecuacion Lineal [{},{},{}]".format(self.__a,self.__b,self.__c)
a,b,c=map(float,input("Ingrese a,b,c:").split())
e1=EcuacionLineal(a,b,c)
if(e1.getDiscriminante()>0):
    print("La ecuacion tiene dos raices",e1.getRaiz1(),"y",e1.getRaiz2())
elif(e1.getDiscriminante()==0):
    print("La ecuacion tiene una raiz",e1.getRaiz1())
else:
    print("La ecuacion no tiene raices reales")
