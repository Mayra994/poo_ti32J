class Silla:
    
    def __init__(self,color,forma,tamaño,asiento,respaldo,comodidad,material,cantidad_patas,marca,precio):
       
        self.color = color
        self.forma = forma
        self.tamaño = tamaño
        self.asiento = asiento
        self.respaldo = respaldo
        self.comodidad = comodidad
        self.material = material
        self.cantidad_patas = cantidad_patas
        self.marca = marca
        self.precio = precio

        print(f"Color: {self.color}")
        print(f"La forma es: {self.forma}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"El asiento es: {self.asiento}")
        print(f"El respaldo es: {self.respaldo}")
        print(f"Comodidad: {self.comodidad}")
        print(f"Material: {self.material}")
        print(f"La cantidad de patas: {self.cantidad_patas}")
        print(f"Marca: {self.marca}")
        print(f"El precio es: {self.precio}")

    def sentarse(self):
        print("Puedes sentarte aquí")
    
    def moverla(self):
        print("Puedes trasladarla a distintos lugares")

    def desarmarla(self):
        print("Puedes desarmarla para ahorrar espacio")

    def reclinar_asiento(self):
        print("Mejora tu comodidad")        

    def subir_en_ella(self):
        print("Puedes usarla para alcanzar objetos altos")

silla = Silla("Negra", "Cuadrada", "1 metro de altura", "Acolchonado", "Respaldo alto", "Muy cómoda", "Cuero sintético", 4, "IKEA", "$150")
silla.sentarse()
silla.moverla()
silla.desarmarla()
silla.reclinar_asiento()
silla.subir_en_ella()