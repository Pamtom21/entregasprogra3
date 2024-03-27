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
# lista=[]
# x= input("Escribe una frase: ")
# identificar(x,lista)
def comunes(lista1, lista2):
    listaux= []
    var=""
    for k in range(len(lista1)):
        for l in range(len(lista2)):
            if lista1[k] == lista2[l]:
                listaux.append(lista1[k])
    if len(listaux) > 3:            
        for m in range(len(listaux)-2):
            if listaux[m] == listaux[m+2] or listaux[m] == listaux[m+1]:
                listaux.remove(listaux[m])
    elif len(listaux) > 2:
        for m in range(len(listaux)-1):
            if listaux[m] == listaux[m+1]:
                listaux.remove(listaux[m])  
            
    print(listaux)
lista1=[]
lista2=[]
for l in range(4):
    x= ra.randint(0,9)
    lista1.append(x)
for l in range(4):
    x= ra.randint(0,9)
    lista2.append(x)
# print(lista1, lista2)
#comunes(lista1,lista2)   