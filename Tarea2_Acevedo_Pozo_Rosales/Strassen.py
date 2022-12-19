import time
import copy

"""
split(a)
Recibe la Matriz que quiere ser separada en 4 cuadrantes.
Return, las 4 sub-matrices formadas
"""

def split(a):
    #Se separa en los 4 cuadrantes, y se forman para cada caso.
    n = len(a)
    lista = []
    lista2 = []
    lista3 = []
    lista4 = []
    #Cuadrante 1 y 2
    for i in range(0, n // 2):
        lista.append(a[i][0:n // 2])
        lista2.append(a[i][n // 2: n])
    #Cuadrante 3 y 4
    for i in range(n // 2, n):
        lista3.append(a[i][0:n // 2])
        lista4.append(a[i][n // 2: n])
    return lista,lista2,lista3,lista4

"""
unir(a,b,c,d)
Recibe 4 matrices, que corresponden a los cuadrantes (sub-matrices) y las une en una sola matriz
retorna la matriz final.
"""
def unir(a,b,c,d):
    n = len(a) #Puede usarse cualquier matriz, ya que todas tienen el mismo tamaño
    lista = [list() for x in range(n*2)]  #Siempre el doble de tamaño, para que entren todas las matrices. #Manera optimizada.
    for i in range(n):  #Primeros dos cuadrantes
        lista[i] = a[i]+b[i]
    for j in range(n):  #Ultimos dos cuadrantes
        lista[n+j] = c[j]+d[j]
    return lista

"""
suma(A,B)
Recibe dos matrices, copia una en otra variabe y suma las matrices en esa nueva matriz.
retorna la Matriz sumada
"""
def suma(A,B):
    C = copy.deepcopy(A)
    n = len(A)
    for i in range(n):
        for j in range(n):
           C[i][j] += B[i][j]
    return C

"""
resta(A,B)
Recibe dos matrices, copia una en otra variabe y resta las matrices en esa nueva matriz.
retorna la Matriz sumada
"""
def resta(A,B):
    C = copy.deepcopy(A)
    n = len(A)
    for i in range(n):
        for j in range(n):
            C[i][j] -= B[i][j]
    return C

"""
Strassen(A,B)
Recibe dos matrices y resuelve el Algoritmo de Strassen para multiplicar matrices
retorna la multiplicación de dos matrices
"""
def Strassen(A,B):
    n = len(A)
    if n ==1:
        Mfinal = [list() for i in range(n)]
        Mfinal[0].append(A[0][0] * B[0][0])
    else:
        #Si se guardan las matrices formadas en distintas variables, esto provoca un aumento excesivo del tiempo de ejecución
        #Lo mejor es referenciarlas para no gastar tanto tiempo!
        a,b,c,d = split(A)
        e,f,g,h = split(B)
        p1 = Strassen(a, resta(f, h))
        p2 = Strassen(suma(a, b), h)
        p3 = Strassen(suma(c, d), e)
        p4 = Strassen(d, resta(g, e))
        p5 = Strassen(suma(a, d), suma(e, h))
        p6 = Strassen(resta(b, d), suma(g, h))
        p7 = Strassen(resta(a, c), suma(e, f))
        cuad11 = suma(suma(p5, p4), resta(p6, p2))
        cuad12 = suma(p1, p2)
        cuad21 = suma(p3, p4)
        cuad22 = resta(suma(p5, p1), suma(p3, p7))
        Mfinal = unir(cuad11,cuad12,cuad21,cuad22)  #Lista unida y preparada para ser printeada :D
    return Mfinal

#Abrir casos de prueba creados a través de una pág generadora de matrices online

prueba = str(input("Caso prueba a comprobar:"))

#Abrir el archivo correspondiente al caso de prueba que se quiere revisar y recorrerlo.

file = open("Pruebas/prueba"+prueba+".txt","r")
linea = file.readlines()
for i in range(len(linea)):
    linea[i] = linea[i].strip().split()
    for j in range(len(linea[i])):
        linea[i][j] = int(linea[i][j]) #Lo que tiene el archivo de forma lista de listas.

N = linea[0][0] #La primera posición, es el valor de N
MatrizA = linea[1:N+1]      #Desde el primer valor hasta el valor que se encuentra en la mitad
MatrizB = linea[N+1:N*2+1]  #Desde la mitad+1, hasta el final del archivo.

#Inicio Main
inicio = time.perf_counter() #Tiempo de ejecución
Valor = Strassen(MatrizA,MatrizB) #Algoritmo de Strissen para calcular la multiplicación de matrices.
final = time.perf_counter() #Como se obtuvo la matriz final, se guarda el tiempo final

#Se printea el largo de la matriz final,

print(str(len(Valor)))  #Valor de N
#Printear cada linea de la matriz

for i in Valor:
    for x in i:
    # imprimir sin salto de línea. Usando un espacio al final
        print(x, end=" ")
    print("")

print("Tiempo de ejecución:", final-inicio ,"segundos")
file.close()