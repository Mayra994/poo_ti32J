class Celular:
    def __init__(self,pantalla,pila,sensores,infrarrojo,botones,bocinas,touch,camaras,centro_carga,color):
        self.pantalla = pantalla
        self.pila = pila
        self.sensores = sensores
        self.infrarrojo = infrarrojo
        self.botones = botones
        self.bocinas = bocinas
        self.touch = touch
        self.camaras = camaras
        self.centro_carga = centro_carga
        self.color = color

        print(f"Pantalla que usa:{self.pantalla}")
        print(f"Pila:{self.pila}")
        print(f"Sensores:{self.sensores}")
        print(f"Infrarrojo:{self.infrarrojo}")
        print(f"Botones:{self.botones}")
        print(f"Bocinas:{self.bocinas}")
        print(f"Touch:{self.touch}")
        print(f"Camaras:{self.camaras}")
        print(f"Centro de carga:{self.centro_carga}")
        print(f"Color:{self.color}")

    def llamar(self):
        print("Puedes realizar llamadas")   

    def enviar_mensajes(self):
        print("Puedes enviar mensajes de texto")

    def tomar_fotos(self):
        print("Puedes tomar fotos")   

    def reproducir_musica(self):
        print("Puedes escuchar tus canciones favoritas")   

    def apagar(self):
        print("Puedes apagar tu celular")           

Samsung_S24_Ultra = Celular("Dynamic AMOLED 2x de 6,8 pulgadas","EB-BS928aby","200mp(ISOCELL hp2sx)", None, "Boton de volumen y boton lateral","Inferior y superior","Sensor ultrasonico","Teleobjetivos con sensor de 50mp","Tipo C","Violeta Titanio")        
Samsung_S24_Ultra.llamar()
Samsung_S24_Ultra.enviar_mensajes()
Samsung_S24_Ultra.tomar_fotos()         
Samsung_S24_Ultra.reproducir_musica()
Samsung_S24_Ultra.apagar()