class LibroBiblioteca:
    def __init__(self,portada,pasta,cantidad_hojas,total_letras,genero,dedicatoria,autor,tipografia,personajes,editorial):
        self.portada = portada
        self.pasta = pasta
        self.cantidad_hojas = cantidad_hojas
        self.total_letras = total_letras
        self.genero = genero
        self.dedicatoria = dedicatoria
        self.autor = autor
        self.tipografia = tipografia
        self.personajes = personajes
        self.editorial = editorial

        print(f"Portada:{self.portada}")
        print(f"Pasta:{self.pasta}")
        print(f"Cantidad de hojas:{self.cantidad_hojas}")
        print(f"Total de letras:{self.total_letras}")
        print(f"Genero:{self.genero}")
        print(f"Dedicatoria:{self.dedicatoria}")
        print(f"Autor:{self.autor}")
        print(f"Tipografía:{self.tipografia}")
        print(f"Personajes:{self.personajes}")
        print(f"Editorial:{self.editorial}")

    def leer(self):
        print("Leer un libro")

    def imaginar(self):
        print("Imaginar la situación")

    def aprender(self):
        print("Aprender algo que te ayude")

    def coleccionar(self):
        print("Ordena el libro en orden")
         
    def reflexionar(self):
        print("Enfocate en lo que esta sucediendo") 

al_final_mueren_los_dos = LibroBiblioteca("portada.jpg","Blanda","352","335,00","Novela juvenil","Para los que estan perdidos","Adam Silvera","Sans-serif","Mateo Torrez Rufus Emeterio","Puck")
al_final_mueren_los_dos.leer()
al_final_mueren_los_dos.imaginar()
al_final_mueren_los_dos.aprender()
al_final_mueren_los_dos.coleccionar()
al_final_mueren_los_dos.reflexionar()
