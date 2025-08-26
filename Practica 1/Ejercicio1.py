class EcuacionLineal:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def tieneSolucion(self):
        s=(self.__a*self.__d)-(self.__b*self.__c)
        if(s==0):
            return False
        return True
    def getX(self):
        if(self.tieneSolucion()):
            x = ((e * d) - (b * f)) / ((a * d) - (b * c))
            return x
    def getY(self):
        if(self.tieneSolucion()):
            y = ((a * f) - (e * c)) / ((a * d) - (b * c))
            return y
    def __str__(self):
        return "Ecuacion Lineal [{},{},{},{},{},{}]".format(self.__a,self.__b,self.__c,self.__d,self.__e,self.__f)
a,b,c,d,e,f=map(float,input("Ingrese a,b,c,d,e,f:").split())
e1=EcuacionLineal(a,b,c,d,e,f)
if(e1.tieneSolucion()):
    print("x=",e1.getX(),", y=",e1.getY())
else:
    print("La ecuacion no tiene solucion")
