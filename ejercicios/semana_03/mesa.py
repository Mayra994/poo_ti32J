class Mesa:
    def __init__(self,color,tamaño,forma,cantidad_patas,material,altura,ensamble,resistencia,peso,dureza):

        self.color = color
        self.tamaño = tamaño
        self.forma = forma
        self.cantidad_patas = cantidad_patas
        self.material = material
        self.altura = altura
        self.ensamble = ensamble
        self.resistencia = resistencia
        self.peso = peso
        self.dureza = dureza


        print(f"El color de la mesa es: {self.color}")
        print(f"El tamaño es: {self.tamaño}")
        print(f"La forma que tiene: {self.forma}")
        print(f"La cantidad de patas es: {self.cantidad_patas}")
        print(f"El materiales: {self.material}")
        print(f"La altura de la mesa es: {self.altura}")
        print(f"El ensamble es: {self.ensamble}")
        print(f"La resistencia es: {self.resistencia}")
        print(f"El peso es: {self.peso}")
        print(f"La dureza es: {self.dureza}")

    def usarlaComedor(self):
        print("Puedes comer aquí")

    def escritorio(self):
        print("Puedes estudiar en esta mesa")

    def soportarObjetos(self):
        print("Puedes colocar objetos pesados sobre esta mesa")

    def moverla(self):
        print("Puedes mover la mesa a diferentes lugares")

    def armarla(self):
        print("Sigue las instrucciones ")

mesa_redonda = Mesa("Marrón", "1.5 metros de diámetro", "Redonda", 4, "Madera", "75 cm", "Tornillos y pegamento", "Alta resistencia", "20 kg", "Dureza media")      
mesa_redonda.usarlaComedor()
mesa_redonda.escritorio()
mesa_redonda.soportarObjetos()
mesa_redonda.moverla()
mesa_redonda.armarla()