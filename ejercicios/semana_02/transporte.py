class Transporte:
    def __init__(self, llantas,ventanas,volante,motor,costo,accesibilidad,seguridad,capacidad,confiabilidad,mantenimiento):
        
        self.llantas = llantas
        self.ventanas = ventanas
        self.volante = volante
        self.motor = motor
        self.costo = costo
        self.accesibilidad = accesibilidad
        self.seguridad = seguridad
        self.capacidad = capacidad
        self.confiabilidad = confiabilidad
        self.mantenimiento = mantenimiento


        print(f"Llantas: {self.llantas}")
        print(f"Las ventanas son: {self.ventanas}")
        print(f"El volante es: {self.volante}")
        print(f"Motor que usa: {self.motor}")
        print(f"Costo a pasajeros: {self.costo}")
        print(f"Accesibilidad: {self.accesibilidad}")
        print(f"Seguridad: {self.seguridad}")
        print(f"La capacidad es: {self.capacidad}")
        print(f"Confiabilidad: {self.confiabilidad}")
        print(f"Mantenimiento necesario: {self.mantenimiento}")

autobus = Transporte("6","Panoramicas","Hidraulicas","Diesel euro VI","12.00 MXN","Rampa y espacio para perro guia","Boton de panico","45 pasajeros","Cada ciertos minutos","Verificacion ambiental semestral")
