import funciones as f

while True :
  
    signo=input("decime si queres una suma, resta, division, multiplicacion, ans o salir: ")
    if signo == "suma" :
        a, b= f.datos()
        ans = f.suma(a,b)
        print("el resultado de la suma es;", ans)
    elif signo == "resta" :
        a, b= f.datos()
        ans = f.resta(a,b)
        print("el resultado de la resta es", a-b)
    elif signo == "multiplicacion" :
        a, b=f.datos()
        ans = f.multiplicacion(a,b)
        print("el resultado de la multiplicacion es", a*b)
    elif signo == "division" :
        a, b=f.datos()
        ans = f.division(a,b)
        if b!=0:
         print("el resultado de la division es", a/b)
        else:
         print("no se puede dividir entre cero")
    elif signo=="ans":
        z=input("decime si queres unas suma, resta, multiplicacion o dividir -con el ans: ")
        if z == "suma" :
             d= f.datos_simples()
             ans=f.suma(ans,d)
             print("el resultado de la suma es;", ans)
        elif z == "resta" :
             d= f.datos_simples()
             ans=f.resta(ans,d)
             print("el resultado de la resta es", ans)
        elif z == "multiplicacion" :
                d=f.datos_simples()
                ans=f.multiplicacion(ans,d)
                print("el resultado de la multiplicacion es", ans)
        elif z == "division" :
            d=f.datos_simples()
            ans=f.division(ans,d)
            print("el resultado de la division es", ans)
    else:
        z =="salir" 
        print("se cierra la calculadora")
        break