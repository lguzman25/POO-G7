while True :
    a=int(input("escriba un numero: "))
    b=int(input("escriba otro numero: "))

    signo=input("decime si queres una suma, resta, division, multiplicacion o salir: ")
    if signo == "suma" :
        print("el resultado de la suma es;", a+b)
    elif signo == "resta" :
        print("el resultado de la resta es", a-b)
    elif signo == "multiplicacion" :
        print("el resultado de la multiplicacion es", a*b)
    elif signo == "division" :
        if b!=0:
         print("el resultado de la division es", a/b)
        else:
         print("no se puede dividir entre cero")
    
    else:
        break