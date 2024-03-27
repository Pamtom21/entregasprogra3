import random as ra
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


a=[]
for k in range(3):
    x = input("ingrese una palabra o un numero ")
    a.append(x)
origen= []
for k in a:
    origen.append(k)
var= ""
for l in a:
    var+= l + " "
print(var)  
listaux= []
b=[]
for s in a:
        try:
            varin= int(s)
            if varin % 2 == 0:
                listaux.append(s)
                a.remove(s)
                print(listaux)
        except:
            pass
for s in a:
        try:
            varin= int(s)
        except:
            b.append(s)
for s in range(len(a)):
    if a[s] == b[s]:
        a.remove(a[s])
print(b)
print(a)
varst=""
for m in b:
    varst+= m + "-->"
print(varst)
varin= 1
for j in range(len(a)):
    for l in range(1,int(j)+1):
            varin *= int(l)
    a[j] = str(varin)
print(a)
varsu = 0
listaux = []
for l in range(len(origen)):
        try:
            varin= int(origen[l])
            varsu+= varin
            listaux.append(varin)
        except ValueError:
            pass
promedio = varsu / len(listaux)
print("la suma de los numeros de origen es: ", varsu, "y su promedio es: ", promedio)
c=[]
for k in range(len(b)):
    for l in range(len(b[k])):
        c.append((b[k])[l])
print(c)
d=[]
varc=""
vara=""
for k in c:
    varc+=k
for m in a:
    vara+= m

        
        
    
    

            
    
            
                       
                
    