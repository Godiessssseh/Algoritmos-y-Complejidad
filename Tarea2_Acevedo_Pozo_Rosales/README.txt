Entrada de datos:

La entrada debe hacerse vía archivos.txt, en la carpeta Pruebas/prueba"n".txt, donde n es un de 2**n
Donde la primera línea del .txt contenga el N, y el resto contenga las 2 matrices separada por espacios
(Se adjuntará unos casos de prueba para que se entienda)

Si quiere probar algun otro caso, agregar un .txt con el siguiente formato (Ejemplo n=2):

Pruebas/prueba2.txt
2	//Valor de N
1 2	//Comienza Matriz 1
3 4
5 6	//Comienza Matriz 2  
7 8	
---------------------------------------------------------------------------------------------------------------------
Se uso Python3 en la resolución de esta tarea en PyCharm, aunque se puede correr en cualquier editor de código
También se probó en una línea de comandos (WSL), donde se hace:

make Strassen
    correrá el algoritmo de Strassen.

make Clasico
    correrá el algoritmo Clasico.

Al correr debe elegir un valor entre 1 hasta 512, donde los últimos archivos toman una cantidad CONSIDERABLE
de tiempo de ejecución (mucho tiempo, a veces 1 min a 6-7 min :c)
----------------------------------------------------------------------------------------------------------------------
Observaciones:
1) Se usó la libreria copy, para usar copy.deepcopy() y copiar una matriz en otra.
2) Intentamos optimizar, se nos triplicó el tiempo, optimizamos de nuevo, se duplicó, esto es lo mejor que pudímos hacer.