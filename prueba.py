var= "hola"
var2 = ""
lista= []
for k in range(len(var)):
    lista.append(var[k])
print(lista)
lista[0]= "p"
for j in range(len(lista)):
    var2 += lista[j]
print(var2)