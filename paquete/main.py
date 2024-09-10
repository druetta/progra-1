import crudStock
import crudCliente
#Programa Principal
electrodomesticos=[ 
    [1,"heladera",110000, 9],
    [2,"horno",95000,8],
    [3,"microondas",56000, 2],
    [4,"lavarropas",136000, 15],
    [5,"horno electrico",110000,12],
    [6,"secadora",123000,10]
]
clientes = {
    "37.647.543": {"nombre": "Juan Perez", "email": "jperez@gmail.com", "telefono": "344-657689"},
    "28.453.789": {"nombre": "Maria Lopez", "email": "mlopez@hotmail.com", "telefono": "341-765432"},
    "32.987.654": {"nombre": "Carlos Garcia", "email": "cgarcia@yahoo.com", "telefono": "342-987654"},
    "23.456.789": {"nombre": "Ana Martinez", "email": "amartinez@gmail.com", "telefono": "343-876543"},
    "39.654.321": {"nombre": "Luis Rodriguez", "email": "lrodriguez@outlook.com", "telefono": "344-234567"},
    "25.678.432": {"nombre": "Sofia Gonzalez", "email": "sgonzalez@hotmail.com", "telefono": "345-345678"},
}

historial_compra = []

ingreso = int(input("1-Gestion de datos 2-Compras "))#Administrar datos 
if ingreso == 1:
    if input("contraseña: ") == "admin": #Controlar acceso
        #Menu C.R.U.D de stock
        print("1-Ingresar un nuevo electrodomestico")
        print("2-Imprimir matriz")
        print("3-Actualizar precio")
        print("4-Eliminar electrodomestico")
        print("5-Ordenar por precio (-1 para salir)")
        opcion = int(input())
        while opcion != -1:
            if opcion == 1:
                producto = int(input("heladera/horno/microondas/lavarropas/horno electrico/secadora (1-6)"))
                crudStock.crear(electrodomesticos,producto)
                print("Producto agregado")
            if opcion == 2:
                crudStock.leer(electrodomesticos) 
            if opcion == 3:
                crudStock.actualizar_precio(electrodomesticos)
            if opcion == 4:
                electrodomesticos = crudStock.eliminar(electrodomesticos)
            if opcion == 5:
                crudStock.ordenar(electrodomesticos)
            opcion = int(input("Desea hacer algo mas(1-5) o -1 "))
else:
    print("1-Nuevo cliente")
    print("2-Imprimir matriz clientes")
    print("3-Actualizar email-telefono")
    print("4-Eliminar cliente")
    print("5-Comprar producto (-1 para salir)")
    opcion_cliente = int(input())
    while opcion_cliente != -1:
            if opcion_cliente == 1:
                crudCliente.crear(clientes)
            if opcion_cliente == 2:
                crudCliente.leer(clientes) 
            if opcion_cliente == 3:
                crudCliente.actualizar_cliente(clientes)
            if opcion_cliente == 4:
                cliente = crudCliente.eliminar(clientes)
            if opcion_cliente == 5:            
                dni = input("DNI XX.XXX.XXX" )
                compra = int(input("heladera/horno/microondas/lavarropas/horno electrico/secadora (1-6)"))
                historial_compra.append([dni,compra])
            opcion_cliente = int(input("Desea hacer algo mas(1-5) o -1 para salir "))