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
    varalf="abcdefghijklmnopqrstuvwxyz"
    varalfmayus="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tamano= 0
    c=0
    for k in range(len(lista)):
        if len(lista[k]) > tamano:
            c=k
            tamano= len(lista[k])
    print("la palabra mas larga es: ", lista[c])
################################################################################
    var= lista[c]
    varaux = ""
    listaux= []
    for l in range(len(var)):
        listaux.append(var[l])
    for k in range(len(listaux)):
        for m in range(len(varalfmayus)):
            if listaux[k] == varalf[m]:
                listaux[k] = varalfmayus[m]
    for h in range(len(listaux)):
        varaux += listaux[h]
    print("la palabra mas larga todo en mayusculas es: ",varaux)
###################################################################################                 
    tamano= 1000000
    c=0
    p= 0
    for l in range(len(lista)):
        for k in varalf:
            if len(lista[l]) < tamano:
                if (lista[l])[0] == k:
                    c=l
                    tamano= len(lista[l])
                    p=1
    print('la palabra mas corta es: ',lista[c])
    if p == 0:
        print("no hay")
####################################################################################
    var = ""
    varaux = "-1"
    for k in range(len(lista)):
        try: 
            var = int(lista[k])
            varaux = str(k)
        except ValueError:
            var = "-1"
    if varaux != var:
        print("la palabra con solo digitos es: ",lista[int(varaux)])
    else:
        print("no hay palabra con solo digitos")
                    
                
        
                 
                        
def identificar(x,lista):
    x+=" "
    palabra= ""
    for f in range(len(x)):
        if x[f] == " ":
            lista.append(palabra)
            palabra= ""
        else:
            palabra+=x[f]
    verificar(lista)
lista=[]
x= input("Escribe una frase: ")
identificar(x,lista)
    