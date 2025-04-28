def datos():
    a=int(input("ingrse un numero aqui: "))
    b=int(input("ingrese un segundo numero aqui: "))
    return a, b


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
    if b=="0":
        print("no se puede dividir entre cero")
    resultado= a / b
    return resultado


while True :
  
    signo=input("decime si queres una suma, resta, division, multiplicacion o salir: ")
    if signo == "suma" :
        a, b= datos()
        print("el resultado de la suma es;", a+b)
    elif signo == "resta" :
        a, b= datos()
        print("el resultado de la resta es", a-b)
    elif signo == "multiplicacion" :
        a, b=datos()
        print("el resultado de la multiplicacion es", a*b)
    elif signo == "division" :
        a, b=datos()
        if b!=0:
         print("el resultado de la division es", a/b)
        else:
         print("no se puede dividir entre cero")
    
    else:
        signo=="salir" 
        print("se cierra la calculadora")
        break