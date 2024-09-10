def crear(matriz,id):
    for i in range(len(matriz)):        
        for j in range(len(matriz[0])):
            if id == matriz[i][j]:
                matriz[i][3] += 1
    return matriz

def leer(matriz):
    recortar_nombre = [[id,nombre[:5],precio,stock] for id,nombre,precio,stock in matriz]
    print(f'{"ID":>4} {"Nombre" :>5} {"Precio" :>7} {"stock" :>2} ')
    for id,nombre,precio,stock in recortar_nombre:
        print(f'{id:>4} {nombre :>5} {precio :>7} {stock :>2} ')

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

def ordenar(matriz):
    electro_ordenado = sorted(matriz, key=lambda x:(x[2]),reverse=True)
    leer(electro_ordenado)
