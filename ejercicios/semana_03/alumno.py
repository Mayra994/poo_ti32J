class Alumno:

    def __init__(self,matricula,nombre,promedio,asignaturas,asistencia,edad,genero,semestre_cuatrimestre,carrera,estatus):

        self.matricula = matricula
        self.nombre = nombre
        self.promedio = promedio
        self.asignaturas = asignaturas
        self.asistencia = asistencia
        self.edad = edad
        self.genero = genero
        self.semestre_cuatrimestre = semestre_cuatrimestre
        self.carrera = carrera
        self.estatus = estatus

        print(f"Matricula: {self.matricula}")
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Promedio actual: {self.promedio}")
        print(f"Asignaturasa: {self.asignaturas}")
        print(f"Porcentaje de asistencias: {self.asistencia}")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero}")
        print(f"Semestre o cuatrimestre: {self.semestre_cuatrimestre}")
        print(f"Carrera: {self.carrera}")
        print(f"Estatus: {self.estatus}")

    def revisarHorario(self):
        print("Revisa tu horario de clases")

    def asistirClase(self):
        print("Asiste puntualmente a todas tus clases")

    def entregarTareas(self):
        print("Entrega tus tareas en tiempo y forma") 

    def presentarExamen(self):
        print("Realiza tu examen")

    def graduarse(self):
        print("Has conseguido graduarte")  

jocelin_valeriano =Alumno("1725110276","Jocelin Valeriano", 9.5, "Integradora 1, POO, Ingles", "95%", 19, "Femenino", "3er cuatrimestre", "Tecnologías de la información e innovación digital", "Activo")
jocelin_valeriano.revisarHorario()
jocelin_valeriano.asistirClase()
jocelin_valeriano.entregarTareas()
jocelin_valeriano.presentarExamen()
jocelin_valeriano.graduarse()
                         