class Mascota:
    def __init__(self, nombre, especie): 
        self.nombre=nombre
        self.especie=especie
        self.felicidad=70
        self.energia=70
        self.hambre=70

    def jugar(self):
        self.felicidad=+15
        self.energia=-10
        self.hambre=-10
        self.felicidad=max(0,min(100, self.felicidad))
        print(f"¡(self.nombre) corretea feliz! su felicidad subio")

    def comer(self):
        self.felicidad=+5
        self.energia=+10
        self.hambre=-40
        self.energia=max(0,min(100, self.energia))
        print(f"¡(self.nombre) devoró su comida con ganas! Ya no tiene tanta hambre.")

    def dormir(self):
        self.felicidad=-10
        self.energia=+60
        self.hambre=-10
        self.dormir=max(0,min(100, self.dormir))
        print(f"¡(self.nombre) está echando una siesta! Se ve más enérgico.")

    def mostrat_estado(self):
        print(f"estado de (self.nombre) (self.especie):")