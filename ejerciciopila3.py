import random as ra           
class pila:
    def __init__(self):
        self.arreglo = []
        self.tope = -1
        self.MAX_ELEMENTS = 3
        self.data = 0 # se agrega este atributo como una variable de control, para contener la suma de todos los enteros de la lista para ser utilizado en getTope, para que en el caso de que la pila este vacia retorne un numero mayor al mas grande ingresado
        for k in range(self.MAX_ELEMENTS):
            self.arreglo.append(None)
    def apilar(self,x):
        if self.tope < self.MAX_ELEMENTS - 1:
            self.tope+=1
            self.arreglo[self.tope] = x
        else:
            print("arreglo lleno ") 
    def desapilar(self):
        if self.isEmpty() == False:
            x = self.tope
            var = self.arreglo[x]
            self.dato+=var
            self.arreglo[x] = None
            self.tope -= 1
            return var
    def getTope(self):
        if self.isEmpty() == False:
            return (self.arreglo[self.tope])
        else:
            return self.data
    def isEmpty(self):
        if self.tope == -1:
            return True
        else:
            return False
    def imprimir(self):
        if self.isEmpty() != True:
            var= ""
            for k in range(0, self.tope+1):
                var += str(self.arreglo[k]) + "|"
            return var
        else:
            return f"La Lista esta vacia"   
p1= pila()
p2 = pila()
p3= pila()
for k in range(p1.MAX_ELEMENTS):
    p1.apilar(ra.randint(0,999))
print("Pila desordenada: ",p1.imprimir())
while True:
    if p3.tope + 1 == p3.MAX_ELEMENTS:
        break
    else:
        if p2.isEmpty() == True:
            p2.apilar(p1.desapilar())
        elif p2.getTope() >= p1.getTope():
            p2.apilar(p1.desapilar())
        elif p3.isEmpty() == True:
            p3.apilar(p2.desapilar())
        else:
            if p3.isEmpty() == False:
                if p3.getTope() > p2.getTope():
                    p1.apilar(p3.desapilar())
                else:
                    p3.apilar(p2.desapilar())
print("Pila ordenada: ",p3.imprimir())

