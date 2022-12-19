import time

"""
producto_matrices(a,b)
Recibe dos matrices (ambas del mismo nxn) y las multiplica.
Retorna la multiplicación entre ambas
"""

def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    # Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto

#Aca se abren los archivos de prueba, donde se crearon casos hasta matrices de 512x512
#Se obtiene el N, y luego se obtiene una lista de todas los valores que hay dentro. Se corta la lista en 2 y se obtienen las matrices
prueba = str(input("Caso prueba a comprobar:"))
file = open("Pruebas/prueba"+prueba+".txt", "r")
linea = file.readlines()
for i in range(len(linea)):
    linea[i] = linea[i].strip().split()
    for j in range(len(linea[i])):
        linea[i][j] = int(linea[i][j])

N = linea[0][0] #El primer valor es el N que tendrán las dos matrices
MatrizA = linea[1:N+1]      #El primer valor hasta la mitad de la matriz
MatrizB = linea[N+1:N*2+1]  #La mitad +1 de la matriz hasta el final de la matriz

#Inicia el código para correr el tiempo
inicio = time.perf_counter()
producto = producto_matrices(MatrizA,MatrizB)
fin = time.perf_counter() #Finalizar el tiempo

#Se imprime el valor que tiene N, y luego cada valor que hay en la lista
print(N)
for i in producto:
        for x in i:
            # imprimir sin salto de línea. Usando un espacio al final
            print(x, end=" ")
        print("")
print("Tiempo de ejecución:", fin-inicio ,"segundos")
file.close()