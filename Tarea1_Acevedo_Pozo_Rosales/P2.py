"""
Es idéntico al trabajado en la pregunta 1 (codigo reciclado)
Join
Parametros: 
N = cantidad de atributos de la 1ra relacion
M = Cantidad de atributos de la 2da relacion
atriR = Atributos de 1ra relación
atriS = Atributos de 2da relación
tabla1 = Lista con todas las tuplas de la relación 1
tabla2 = Lista con todas las tuplas de la relación 2
Resumen: Hace un Join entre los valores que se le den, en este caso los del triangulo
Salida: Lista de listas con los Join entre los valores dados del triangulo
"""
def Join(N, M, atriR, atriS, tabla1, tabla2):
    atr_iguales = list(set(atriR) & set(atriS))
    atr_iguales.sort()
    L = len(atr_iguales)
    atr_T = list(set(atriR) | set(atriS))
    atr_T.sort()

    tablaT = []
    posAtrR = []
    posAtrS = []
    for elem in atr_iguales:
        posAtrR.append(atriR.index(elem))
        posAtrS.append(atriS.index(elem))

    for filaR in tabla1:
        for filaS in tabla2:
            c = 0
            for i in range(L):
                if filaR[posAtrR[i]] == filaS[posAtrS[i]]:
                    c += 1
                else:
                    break
            if c == L:
                temp = []
                for j in range(N):
                    temp.append((atriR[j], filaR[j]))
                for k in range(M):
                    temp.append((atriS[k], filaS[k]))
                    
                ls_tuplas = list(set(temp))
                ls_tuplas.sort()
                filaT = [tupla[1] for tupla in ls_tuplas]
                tablaT.append(filaT)

    return tablaT
        
'''Aqui comienza el programa para la pregunta 2:'''

#Lista que almacena los inputs
Tabla = list()
#Lista que almacena los triangulos encontrados
match = list() 

#Solicitud de inputs
arco = input("Ingrese arco: ")

while arco!='EOF':
    arcos = list(map(int, arco.split(" ")))
    Tabla.append(arcos)
    arco = input("Ingrese arco: ")

if len(Tabla)!=0:
    #Uso de la funcion Join con los inputs
    tablaT = Join(2, 2, [0,1], [1,2], Tabla, Tabla)
    #Recorremos solucion de lo que entrega Join
    for a, b, c in tablaT:
        #Existe a->b y b->c, pero falta el tercer arco dirigido necesario c->a.
        #Se debe encontrar, y si lo encuentra lo agrega a lista match.
        if ([b,c,a] in tablaT) or ([c,a,b] in tablaT):
            match.append([a,b,c])

#Entrega del resultado
print (int(len(match)/3))

#Se divide en 3 puesto que al hacer el Join, cada triangulo tiene asociado
#sus tres combinaciones posibles.