a=[]
c=0
for i in range (1, 6) :
    b = int(input("ingrese una edad "))
    while b<0 :
          b = int(input("ingrese una edad "))
    a.append(b)
print(a)
while c<5 :
    print(a[c])
    if a[c] < 18 :
          print("es menor de edad")
    elif a[c] < 65 and a[c] > 18 :
          print("son adultos")
    elif a[c] > 65 :
          print("son viejos")
    c= c+1 