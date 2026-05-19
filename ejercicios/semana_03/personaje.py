class Personaje:
    def __init__(self, nombre, edad,color,tamaño,origen,rapidez,vidas,fuerza,vestimenta,proteccion):

        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.tamaño = tamaño
        self.origen = origen
        self.rapidez = rapidez
        self.vidas = vidas
        self.fuerza = fuerza    
        self.vestimenta = vestimenta
        self.proteccion = proteccion

        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Origen: {self.origen}")
        print(f"Rapidez: {self.rapidez}")
        print(f"Vidas: {self.vidas}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Vestimenta: {self.vestimenta}")
        print(f"Protección: {self.proteccion}")


    def correr(self):
        print("vleocidad del personaje")

    def saltar(self):
        print("El personaje puede saltar obstáculos")

    def hablar(self):
        print("El personaje no puede comunicarse con otros personajes")   

    def girar(self):
        print("El personaje gira para romper cajas")

    def disparar(self):
        print("El personaje no puede disparar")    

crash_bandicoot = Personaje("Crash Bandicoot", 30, "Naranja", "1.5 metros", "Isla de Wumpa", "Rápido", 3, "Fuerte", "Pantalones cortos azules y zapatos rojos", None)
crash_bandicoot.correr()
crash_bandicoot.saltar()
crash_bandicoot.hablar()
crash_bandicoot.girar()
crash_bandicoot.disparar()
