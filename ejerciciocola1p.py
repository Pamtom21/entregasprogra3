class cola:
    def __init__(self):
        self.arreglo= []
        self.primero = 0
        self.ultimo = -1
        self.numElem = 0
        self.MAX_ELEM = 3
        for k in range(self.MAX_ELEM):
            self.arreglo.append(None)
    def encolar(self,x):
        if self.numElem < self.MAX_ELEM:
            if (self.ultimo + 1)%self.MAX_ELEM == 0:
                self.ultimo=(self.ultimo + 1)%self.MAX_ELEM
            self.ultimo += 1
            self.numElem+=1
            self.arreglo[self.ultimo]= x
    def sacar(self):
        if self.isEmpty() == False:
            self.primero+=1
            self.numElem-=1
            self.primero=(self)
        else:
            print("cola vacia")
    def isEmpty(self):
        if self.numElem <= 0:
            return True
        else:
            return False
    def imprimir(self):
        var=""
        for k in range(self.numElem):
            var+=str(self.arreglo[k])
        return var
c1= cola()
c1.encolar("1")
c1.encolar("2")
c1.encolar("3")
print(c1.imprimir())