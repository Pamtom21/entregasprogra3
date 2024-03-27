class pila:
    def __init__(self):
        self.arreglo = []
        self.tope = -1
        self.MAX_ELEMENTS = 3
    def apilar(self,x):
        if self.tope < (self.MAX_ELEMENTS -1):
            self.arreglo.append(x)
            self.tope+=1
        else:
            print("arreglo lleno ") 
    def desapilar(self):
        if self.isEmpty() == False:
            self.tope -= 1
    def getTope(self):
        print(self.arreglo[self.tope])
    def isEmpty(self):
        if self.tope == -1:
            print("lista vacia")
            return True
        else:
            return False
    def imprimir(self):
        var= ">"
        for k in range(0, self.tope+1):
            var += self.arreglo[k] + "|"
        print(var)
pila1= pila()
pila1.apilar("1")
pila1.apilar("2")
pila1.apilar("3")
pila1.getTope()
pila1.isEmpty()
pila1.imprimir()
pila1.desapilar()
pila1.getTope()
pila1.imprimir()