class Universidad:

    def  __init__(self, logo, oferta_educativa,localidad, sistema_informatico,modalidad,servicios,ubicacion,talleres,cantidad_salones,rector):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.localidad = localidad
        self.sistema_informatico = sistema_informatico
        self.modalidad = modalidad
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.talleres = talleres 
        self.cantidad_salones = cantidad_salones
        self.rector = rector

        print(f"Logotipo de la universidad:{self.logo}")
        print(f"La oferta educativa es:{self.oferta_educativa}")
        print(f"La localidad es:{self.localidad}")
        print(f"Sistema informatico:{self.sistema_informatico}")
        print(f"Modalidad:{self.modalidad}")
        print(f"Servicios que ofrecen:{self.servicios}")
        print(f"Ubicación:{self.ubicacion}")
        print(f"Talleres que ofrecen:{self.talleres}")
        print(f"Cantidad de salones:{self.cantidad_salones}")
        print(f"Rector:{self.rector}")

    def aprender(self):
        print("Aprende algo nuevo cada día")
        
    def estudia(self):
        print("Estudia para tener un mejor futuro")

    def capacitar(self):
        print("Capacitate para ser mejor")

    def educar(self):
        print("Educa para crear mejores ciudadanos")

    def contratar(self):
        print("Contrata a los mejores profesores")

unideh = Universidad("logo.jpg","Ing.Sistemas,Turismo alternativo","San Miguel","CADU","Virtual","Biblioteca digital","Santa Catarina",None, None,"Octavio Castillo")
unideh.aprender()
unideh.estudia()
unideh.capacitar()
unideh.educar()
unideh.contratar()