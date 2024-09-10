import validaciones 
def crear(diccionario):
    dni = input("DNI (XX.XXX.XXX): ")
    while not validaciones.validar_dni(dni):
        dni = input("Ingrese el formato correcto(XX.XXX.XXX)")
    nombre = input("Nombre: ")
    email = input("Email: ")
    while not validaciones.validar_email(email):
        email = input("Ingrese un email valido")
    telefono = input("Teléfono (XXX-XXXXXX): ")
    while not validaciones.validar_email(email):
        telefono = input("Ingrese un telefono valido (XXX-XXXXXX)")
    diccionario[dni] = {"nombre": nombre, "email": email, "telefono": telefono}
    return diccionario

def leer(diccionario):
    print(f'{"DNI":>12} {"Nombre":>20} {"Email":>25} {"Teléfono":>15}')
    for dni, clave in diccionario.items():
        print(f'{dni:>12} {clave["nombre"]:>15} {clave["email"]:>20} {clave["telefono"]:>15}')

def actualizar_cliente(diccionario):
    dni = input("DNI: ")
    if dni in diccionario:
        email = input("Nuevo Email: ")
        telefono = input("Nuevo Teléfono: ")
        diccionario[dni]["email"] = email
        diccionario[dni]["telefono"] = telefono
    else:
        print("No se encontro el cliente")
    return diccionario

def eliminar(diccionario):
    dni = input("DNI: ")
    if dni in diccionario:
        del diccionario[dni]
        print("Cliente eliminado")
    else:
        print("No se encontro el cliente")
    return diccionario


