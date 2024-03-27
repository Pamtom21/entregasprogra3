def busquedanombre(lista,letra):
    listaux = []
    for k in range(len(lista)):
            if (lista[k])[0] == letra:
                listaux.append(lista[k])
    print("Los nombres que corresponden a la letra: ", letra, " es ", listaux)
lista=[]
# for a in range(4):
#     x = input("ingrese nombres: ")
#     lista.append(x)
#busquedanombre(lista, input("Ingrese una letra: "))