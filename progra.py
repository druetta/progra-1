import random

def crear_matriz(fil,col):
    '''
    pre: recibe numero de estudiantes y materias 
    pos: devuelve una matriz donde estuiantes = filas y materias = columnas
    '''
    return [[0] * col for i in range(fil)]

def llenar_matriz(matriz):
    '''
    pre: recibe la matriz creada 
    pos: la rellena con numeros aleatorios
    '''
    fila = len(matriz)
    columna = len(matriz[0])
    for i in range(fila):
        for j in range(columna):
            num = random.randint(1,10)
            matriz[i][j] = num

def mostrar_matriz(matriz,estuiantes,materias):
    '''
    pre: recibe matriz estudiantes y materias
    pos: la imprime de manera ordenada
    '''
    for i in range(estuiantes):
        for j in range(materias):
            print("%4d" % matriz[i][j], end="")
        print()

def calcular_promedio_estudiantes(matriz):
    '''
    pre: recibe la matriz
    pos: calcula el promedio de cada estudiante
    '''
    estudiante = len(matriz)
    materia = len(matriz[0])
    for i in range(estudiante):
        promedio = 0
        for j in range(materia):
            promedio += matriz[i][j]
        print(f"El promedio del estudiante {i+1} es de {promedio/materia}")

def calcular_promedio_materias(matriz):
    '''
    pre: recibe la matriz como parametro
    pos: calcula el promedio de cada columna
    '''
    estudiante = len(matriz)
    materia = len(matriz[0])
    promedio_materia = [0] * materia
    for i in range(estudiante):
        for j in range(materia):
            promedio_materia[j] += matriz[i][j]
    for x in range(materia):    
        print(f"El promedio la materia {x+1} es de {promedio_materia[x]/estudiante}")
            
#Programa principal
filas = int(input("estudiantes "))
columnas = int(input("materias "))
M = crear_matriz(filas,columnas)
llenar_matriz(M)
mostrar_matriz(M,filas,columnas)
calcular_promedio_estudiantes(M)
calcular_promedio_materias(M)