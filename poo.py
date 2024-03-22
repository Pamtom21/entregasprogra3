#1
import random as ra
class jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.vida = 100
        self.estado = True
    def shoot(self, jugador):
        if self.estado == True:
            print(f"{self.nombre} a disparado a {jugador.nombre}")
    def info(self):
        if self.estado == True:
            print(f"el jugador {self.nombre} esta vivo \nVida: {self.vida} ")
        else:
            print(f"el jugador {self.nombre} no se encuentra vivo")
    def heal(self,x):
        if self.estado == True:
            if self.vida == 100:
                print(f"El personaje {self.nombre} ya se encuentra al maximo de vida")
            else:
                self.vida+= x
                if self.vida > 100:
                    self.vida= 100
                print(f"El jugador {self.nombre} se ha curado {x} su nueva vida es {self.vida} ")
    def dmg(self,x):
        if self.estado == True:
            self.vida-= x
            if self.vida <= 0:
                self.vida = 0
                self.estado = False
                print(f"El jugador {self.nombre} a muerto")
            else:
                print(f"El jugador {self.nombre} a recibido {x} daño su nueva vida es {self.vida} ")
j1=jugador("Spike")
j2=jugador("Azazel")
j3=jugador("Lilith")
listaj= [j1,j2,j3]
while True:
    for k in range(len(listaj)-1):
        if listaj[k].vida <= 0:
            listaj.remove(listaj[k])
    if len(listaj) < 2:
       print(f"El jugador {listaj[0].nombre} es el ganador") 
       break
    else:
        if j1.estado == True:
            op=ra.randint(0,1)
            if op == 0:
                opj= ra.randint(0,1)
                if opj == 0:
                    juga = j2
                    if juga.estado == False:
                        juga = j3
                elif opj == 1:
                    juga= j3
                    if juga.estado == False:
                        juga = j2                    
                j1.shoot(juga)
                dano= ra.randint(50, 100)
                juga.dmg(dano)
            elif op== 1:
                h= ra.randint(10, 30)
                j1.heal(h)
            j1.info()
            x=input("")
###########################################################
        if j2.estado == True:
            op=ra.randint(0,1)
            if op == 0:
                opj= ra.randint(0,1)
                if opj == 0:
                    juga = j1
                    if juga.estado == False:
                        juga = j3
                elif opj == 1:
                    juga= j3
                    if juga.estado == False:
                        juga = j1
                j2.shoot(juga)
                dano= ra.randint(50, 100)
                juga.dmg(dano)
            elif op== 1:
                h= ra.randint(10, 30)
                j2.heal(h)
            j2.info()
            x=input("")
#################################################################
        if j3.estado == True:
            op=ra.randint(0,1)
            if op == 0:
                opj= ra.randint(0,1)
                if opj == 0:
                    juga = j2
                    if juga.estado == False:
                        juga = j1
                elif opj == 1:
                    juga= j1
                    if juga.estado == False:
                        juga = j2
                j3.shoot(juga)
                dano= ra.randint(50, 100)
                juga.dmg(dano)
            elif op== 1:
                h= ra.randint(10, 30)
                j3.heal(h)
            j3.info()
            x=input("")    
        
