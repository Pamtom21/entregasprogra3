def invertir(x,y):
     for l in x[::-1]:
         y.append(l)
     print(y)
lista=[]
listanueva=[]

while True:
     op= input("1 para agregar elementos o 2 para invertir lista o 3 para salir ")
     if op == "3":
         break
     elif op == "1":
        elements=input("ingrese algo: ")
        for k in range(len(elements)):
            lista.append(elements[k])
        print(lista)
     elif op == "2":
         invertir(lista, listanueva)
         lista = []