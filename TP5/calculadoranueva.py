import funciones as f

while True :
  
    signo=input("decime si queres una suma, resta, division, multiplicacion o salir: ")
    if signo == "suma" :
        a, b= f.datos()
        print("el resultado de la suma es;", a+b)
    elif signo == "resta" :
        a, b= f.datos()
        print("el resultado de la resta es", a-b)
    elif signo == "multiplicacion" :
        a, b=f.datos()
        print("el resultado de la multiplicacion es", a*b)
    elif signo == "division" :
        a, b=f.datos()
        if b!=0:
         print("el resultado de la division es", a/b)
        else:
         print("no se puede dividir entre cero")
    elif signo=="ans":
         z=input("decime si queres unas sumaresta,multiplicacion o dividir-con el ans")
         ñ=int(input"ahora dame el numero con el que eueres hacer la operacion: ")
         if signo == "suma" :
             a, b= f.datos()
             print("el resultado de la suma es;", a+b)
         elif signo == "resta" :
             a, b= f.datos()
             print("el resultado de la resta es", a-b)
         elif signo == "multiplicacion" :
              a, b=f.datos()
                print("el resultado de la multiplicacion es", a*b)
         elif signo == "division" :
        a, b=f.datos()
    else:
        signo=="salir" 
        print("se cierra la calculadora")
         break