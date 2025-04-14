a=input("ingrse una palabra o frase ")
v=0
c=0
while a == " " :
    a = input("ingrse una palabra o frase ")
for i in a :
    if i == "a" or i == "e" or i == "u" or i == "o" or i == "i" :
         v+=1
    else :
        c+=1
if v>5 :
    a = input ("ingrse otra palabra o frase ")
print (v ,"es la cantidad de vocales ")
print  (c, "es la cantidad de consonantes")