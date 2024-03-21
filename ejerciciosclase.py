# #arreglos
# def invertir(x,y):
#     n= len(x) - 1
#     for l in x[::-1]:
#         y.append(l)
#     print(y)
# lista=[]
# listanueva=[]

# while True:
#     op= input("1 para agregar elementos o 2 para invertir lista o 3 para salir")
#     if op == "3":
#         break
#     elif op == "1":
#         elements=input("ingrese algo: ")
#         lista.append(elements)
#     elif op == "2":
#         invertir(lista, listanueva)
#2
def verificar(lista):
    tamano= 0
    c=0
    for k in range(len(lista)):
        if len(lista[k]) > tamano:
            c=k
            tamano= len(lista[k])
    print("la palabra mas larga es: ", lista[c])
    tamano= 100
    c=0
    p= 0
    var="abcdefghijklmnopqrstuvwxyz"
    for l in range(len(lista)):
        for k in var:
            if len(lista[l]) < tamano:
                if (lista[l])[0] == k:
                    c=l
                    tamano= len(lista[l])
                    p=1
                    print(lista[c])
    if p == 0:
        print("no hay")
                 
                



        
def identificar(x,lista):
    x+=" "
    palabra= ""
    for f in range(len(x)):
        if x[f] == " ":
            lista.append(palabra)
            palabra= ""
        else:
            palabra+=x[f]
    print(lista)
    verificar(lista)
lista=[]
x= input("Escribe una frase: ")
identificar(x,lista)
    