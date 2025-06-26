class Mascota:
    def __init__(self, nombre, especie): 
        self.nombre=nombre
        self.especie=especie
        self.felicidad=50
        self.energia=50
        self.hambre=50

    def ajustar_valores(self):
        if self.felicidad > 100:
            self.felicidad = 100
        elif self.felicidad < 0:
            self.felicidad = 0

        if self.energia > 100:
            self.energia = 100
        elif self.energia < 0:
            self.energia = 0

        if self.hambre > 100:
            self.hambre = 100
        elif self.hambre < 0:
            self.hambre = 0

    def jugar(self):
        self.felicidad += 15
        self.energia -= 10
        self.hambre += 10
        self.ajustar_valores()
        print(f"{self.nombre} corre feliz")

    def comer(self):
        self.hambre -= 30
        self.energia += 5
        self.ajustar_valores()
        print(f"{self.nombre} devoró su comida")

    def dormir(self):
        self.energia += 25
        self.felicidad -= 5
        self.hambre += 10
        self.ajustar_valores()
        print(f"{self.nombre} esta durmiendo")
        


    def mostrar_estado(self):
        print("Estado de la mascota")
        print("Nombre:", self.nombre)
        print("Especie:", self.especie)
        print("Felicidad:", self.felicidad)
        print("Energía:", self.energia)
        print("Hambre:", self.hambre)

        if self.felicidad >= 90:
            print("Está feliz")
        elif self.felicidad <= 30:
            print("Está triste")

        if self.energia >= 90:
            print("Tiene energia")
        elif self.energia <= 30:
            print("Está cansado")

        if self.hambre >= 80:
            print("Tiene hambre")
        elif self.hambre <= 20:
            print("Está lleno")


name=input("elegi un nombre para tu mascota: ")
tipo=input("elegi q especie es(perro,gato,dragon,araña,serpiente): ")

mascota1=Mascota(name,tipo)


while True:
    print("¿Qué querés hacer con tu mascota?")
    print("1. Jugar")
    print("2. Comer")
    print("3. Dormir")
    print("4. Ver estado")
    print("5. Salir")
    
    opcion = input("Elegí una opción (1-5): ")

    if opcion == "1":
        mascota1.jugar()
    elif opcion == "2":
        mascota1.comer()
    elif opcion == "3":
        mascota1.dormir()
    elif opcion == "4":
        mascota1.mostrar_estado()
    elif opcion == "5":
        print("Chau")
        break

    else:
        print("Opción no válida. Probá de nuevo.")