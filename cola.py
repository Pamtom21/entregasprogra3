class cola:
    def __init__(self):
        self.arreglo= []
        self.primero = 0
        self.ultimo = -1
        self.numElem = self.ultimo + 1 - self.primero
        self.MAX_ELEM = 3
    def encolar(self,x):
        self.arreglo.append(x)
        self.ultimo += 1
    def sacar(self):
        self.primero+=1
    

