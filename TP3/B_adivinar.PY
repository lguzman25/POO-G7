secreto=60
for i in range (7) :
    numero = int(input("adivina el numero, entre 1 y 100: "))
    if numero == secreto :
        print("ganaste")
        break
    elif numero< secreto :
        print("el numero es mayor")
    elif numero> secreto:
        print("el numero es menor")
    else:
         print("perdiste el numero era:", secreto) 