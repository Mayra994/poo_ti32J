class Perro:
    def __init__(self, color, raza, tamaño,cola, colmillos,orejas,color_ojos,olfato, temperamento,sendibilidad):
        self.color = color
        self.raza = raza
        self.tamaño = tamaño
        self.cola = cola
        self.colmillos = colmillos
        self.orejas = orejas
        self.color_ojos = color_ojos
        self.olfato = olfato
        self.temperamento = temperamento
        self.sendibilidad = sendibilidad

        print(f"Color: {self.color}")
        print(f"Raza: {self.raza}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Cola: {self.cola}")
        print(f"Colmillos: {self.colmillos}")
        print(f"Orejas: {self.orejas}")
        print(f"Color de ojos: {self.color_ojos}")
        print(f"Olfato: {self.olfato}")
        print(f"Temperamento: {self.temperamento}")
        print(f"Sensibilidad: {self.sendibilidad}")

    def comer(self):
        print("El perro come croquetas")

    def ladrar(self):
        print("El perro ladra")

    def correr(self):
        print("El perro corre por el parque")

    def morder(self):
        print("El perro muerde un hueso")
        
    def hacerDelBaño(self):
        print("El perro hace del baño en el jardín")

kira =Perro("Negro y cafe","Chihuahua","Pequeño","Corta","Blancos","Medianas","Cafes","Muy agudo","Tranquilo","Alta")
kira.comer()
kira.ladrar()
kira.correr()
kira.morder()
kira.hacerDelBaño()