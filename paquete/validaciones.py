import re 

def validar_dni(cad):
    patron = "[0-9]{2}\.[0-9]{3}\.[0-9]{3}"
    if re.match(patron,cad):
        return True
    else:
        return False
    
def validar_email(cad):
    patron = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9]+\.[a-z]+$"
    if re.match(patron,cad):
        return True
    else:
        return False
    
def validar_telefono(cad):
    patron = "[0-9]{3}-[0-9]{6,}"
    if re.match(patron,cad):
        return True
    else:
        return False