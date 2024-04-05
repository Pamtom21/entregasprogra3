class pila:
    def __init__(self):
        self.arreglo = []
        self.tope = -1
        self.MAX_ELEMENTS = 5
        self.tope2 = self.MAX_ELEMENTS
        for k in range(self.MAX_ELEMENTS):
            self.arreglo.append(None)
    def apilar(self,x):
        if self.tope + 1 < self.tope2:
            self.tope+=1
            self.arreglo[self.tope] = x
        else:
            print("Arreglo lleno")
    def apilar1(self,x):
        if self.tope2-1 > self.tope:
            self.tope2-=1
            self.arreglo[self.tope2] = x
        else:
            print("Arreglo lleno")
    def desapilar(self):
        if self.isEmpty() == False:
            self.tope -= 1
        else:
            print("El arreglo esta vacio")
    def desapilar2(self):
        if self.isEmpty2() == False:
            self.tope2 += 1
        else:
            print("El arreglo esta vacio")
    def getTope(self):
        return (self.arreglo[self.tope])
    def getTope2(self):
        return (self.arreglo[self.tope2])
    def isEmpty(self):
        if self.tope == -1:
            return True
        else:
            return False
    def isEmpty2(self):
        if self.tope2 == self.MAX_ELEMENTS:
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
    def imprimir2(self):
        if self.isEmpty() != True:
            var= ""
            for k in range(self.tope2, self.MAX_ELEMENTS):
                var += self.arreglo[k]
            return var
        else:
            return f"La Lista esta vacia"
p1 = pila()

p1.apilar("y")
p1.apilar1("r")
p1.apilar("p")
p1.apilar1("j")
p1.apilar("l")
p1.apilar("a")
print(p1.imprimir())
print(p1.imprimir2())
p1.desapilar2()
p1.desapilar2()
p1.desapilar2()
p1.apilar("t")
print(p1.imprimir())
print(p1.imprimir2())