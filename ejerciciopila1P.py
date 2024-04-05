class pila:
    def __init__(self, MAX_ELEMENTS):
        self.arreglo = []
        self.tope = -1
        self.MAX_ELEMENTS = MAX_ELEMENTS
    def apilar(self,x):
        if self.tope < (self.MAX_ELEMENTS -1):
            self.arreglo.append(x)
            self.tope+=1
        else:
            print("arreglo lleno ") 
    def desapilar(self):
        if self.isEmpty() == False:
            x = self.tope
            self.tope -= 1
            return self.arreglo[x]
    def getTope(self):
        print(self.arreglo[self.tope])
    def isEmpty(self):
        if self.tope == -1:
            return True
        else:
            return False
    def imprimir(self):
        if self.isEmpty() != True:
            var= ""
            for k in range(0, self.tope+1):
                var += self.arreglo[k]
            return var
        else:
            return f"La Lista esta vacia"
x = input("Ingrese una palabra: ")
var = len(x)
p1 = pila(var)
for k in x:
    p1.apilar(k)
p2 = pila(var)
for l in range(var):
    f= p1.desapilar()
    p2.apilar(f)
print(p1.imprimir())
print(p2.imprimir())
    


