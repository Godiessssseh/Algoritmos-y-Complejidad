#Primero se deben insertar la cantidad de atributos que trae la relación R
tablaR = []
N = int(input("Cantidad N de atributos de R: "))
atri = input("Atributos de R: ") #Atributos de la relación R
AtriR = atri.split(" ")

#Luego se ingresa la cantidad de tuplas que trae la relación R
NR = int(input("Cantidad de tuplas de R: "))
for i in range(NR):
    fila_str = input("Ingrese tupla " + str(i+1) +": ") #Se ingresan las tuplas
    #fila_ls = list(map(int, fila_str.split(" ")))
    tablaR.append(list(map(int, fila_str.split(" "))))

#Ahora se ingresan los atributos que trae la relación S

tablaS = []
M = int(input("Cantidad M de atributos de S: "))
atr = input("Atributos de S: ") #Atributos de la relación S
atriS = atr.split(" ")

#Luego se ingresa la cantidad de tuplas que trae la relación S

NS = int(input("Cantidad de tuplas de S: "))
for i in range(NS):
    fila_str = input("Ingrese tupla " + str(i+1) +": ") #Se ingresan las tuplas
    #fila_ls = list(map(int, fila_str.split(" ")))
    tablaS.append(list(map(int, fila_str.split(" "))))

#Empieza el join

atr_iguales = list(set(AtriR) & set(atriS)) #Atributos iguales
atr_iguales.sort()

L = len(atr_iguales)  #Largo de la cantidad de atributos iguales (1)
atr_T = list(set(AtriR) | set(atriS))  #Todos los atributos
atr_T.sort()


tablaT = []
posAtrR = []
posAtrS = []
for elem in atr_iguales: #1
    posAtrR.append(AtriR.index(elem)) #Posicion donde se encuentra en los atributos R (1)
    posAtrS.append(atriS.index(elem)) #Posicion donde se encuentra en los atributos S (0)

for filaR in tablaR: #Cada tupla de R
    for filaS in tablaS: #Cada tupla de S
        contador = 0
        for i in range(L):
            if filaR[posAtrR[i]] == filaS[posAtrS[i]]: #R -> B= 2, s -> B = 2 
                contador += 1 #contador cambia para unirlos todos
            else:
                break
        if contador == L: 
            temp = []
            for j in range(N): #N = 2, j = 0,1
                temp.append((AtriR[j], filaR[j]))
            for k in range(M): #M = 2  k = 0,1
                temp.append((atriS[k], filaS[k]))
            ls_tuplas = list(set(temp)) #Si se repite algun valor, se deja solo 1
            ls_tuplas.sort()
            filaT = [tupla[1] for tupla in ls_tuplas] #Join de R y S
            tablaT.append(filaT) #Relación T

#Relación resultante T. Se muestra por pantalla.

print(len(atr_T)) #Valor de P     
atr_T = " ".join(atr_T)
print(atr_T) #Cantidad de atributos resultantes
print(len(tablaT)) #NT, cantidad de tuplas del join
for row in tablaT:
    row = list(map(str, row))
    print(" ".join(row)) #tuplas del join