def crear(matriz):
    matriz.append([])
    ultima_pos = len(matriz)
    matriz[ultima_pos-1].append(ultima_pos)
    matriz[ultima_pos-1].append(input("Ingrese electrodomestico: "))
    matriz[ultima_pos-1].append(int(input("Ingrese precio:")))
    return matriz

def leer(matriz):
    recortar_nombre = [[id,nombre[:5],precio] for id,nombre,precio in matriz]
    print(f'{"ID":>4} {"Nombre" :>5} {"Precio" :>7} ')
    for id,nombre,precio in recortar_nombre:
        print(f'{id:>4} {nombre :>5} {precio :>7} ')

def actualizar_precio(matriz):
    id = int(input("ID: "))
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            if id == matriz[i][j]:
                matriz[i][2] = int(input("Nuevo precio: "))
    return matriz

def eliminar(matriz):
    id = int(input("ID: "))
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            if id == matriz[i][j]:
                matriz_copia = matriz.copy()
                matriz_copia.pop(i)
    return matriz_copia



#Programa Principal
electrodomesticos=[ 
[1,"heladera",110000],
[2,"horno",95000],
[3,"microondas",56000],
[4,"lavarropas",136000],
[5,"horno electrico",110000],
[6,"secadora",123000]
]
electro_recortado = [[id,nombre[:5],precio] for id,nombre,precio in electrodomesticos]
electro_ordenado = sorted(electro_recortado, key=lambda x:(-x[2],x[1]))
#Menu C.R.U.D
print("1-Ingresar un nuevo electrodomestico\n2-Imprimir matriz\n3-Actualizar precio\n4-Eliminar electrodomestico\n(-1 para salir)\n")
opcion = int(input())
while opcion != -1:
    if opcion == 1:
        crear(electrodomesticos)
    if opcion == 2:
        leer(electrodomesticos) 
    if opcion == 3:
        actualizar_precio(electrodomesticos)
    if opcion == 4:
        electrodomesticos = eliminar(electrodomesticos)
    opcion = int(input("1-Ingresar un nuevo electrodomestico\n2-Imprimir matriz\n3-Actualizar precio\n4-Eliminar electrodomestico\n(-1 para salir)\n"))