def datos():
    a=int(input("ingrse el valor de a: "))
    b=int(input("ingrse el valor de b: "))
    c=int(input("ingrse el valor de c: "))
    return  a, b, c

def vertice (a,b,c) :
    v=(-b/2*a)
    y=(a*v**2 + b*v + c) 
    return v, y