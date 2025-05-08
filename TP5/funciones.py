def datos():
    a=int(input("ingrse un numero aqui: "))
    b=int(input("ingrese un segundo numero aqui: "))
    return a, b

def datos_simples():
    d=int(input("ingrse un numero aqui: "))
    return d

def suma (a, b):
    resultado= a + b
    return resultado

def resta (a, b):
    resultado= a - b
    return resultado

def multiplicacion (a, b):
    resultado= a * b
    return resultado

def division (a, b):
    if b==0:
        print("no se puede dividir entre cero")
    resultado= a / b
    return resultado
