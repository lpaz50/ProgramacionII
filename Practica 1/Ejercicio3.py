import math
class Estadistica:
    def __init__(self,vector):
        self.__vector =vector
    def promedio(self):
        p=0
        for i in range(0,10,1):
            p=p+self.__vector[i]
        return p/len(vector)
    def desviacion(self):
        d=0
        for i in range(0,10,1):
            d=d+((self.__vector[i]-self.promedio())**2)
        return math.sqrt(d/(len(vector)-1))
    def __str__(self):
        return "Estadistica [{}]".format(self.__vector)
vector=[float(i) for i in input().split()]
e1=Estadistica(vector)
print("El promedio es",e1.promedio())
print("La desviacion estandard es",e1.desviacion())
