import matplotlib.pyplot as plt

a=int(input("ingrse el valor de a: "))
b=int(input("ingrse el valor de b: "))
c=int(input("ingrse el valor de c: "))

print("la")

x = []
y = []
inicio = -10
fin = 10
paso = (fin - inicio) / 399  # 400 puntos

for i in range(400):
    valor_x = inicio + i * paso
    x.append(valor_x)
    y.append(a * valor_x**2 + b * valor_x + c)

print("x:", x)
print("y:", y)
# Graficar la función cuadrática
plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
plt.title('Función cuadrática')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()