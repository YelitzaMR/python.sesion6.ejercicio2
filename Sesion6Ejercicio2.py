class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre=nombre
        self.calificacion=calificacion

    def mostrar(self):
        print('Alumno:', self.nombre)
        print('Calificación:', self.calificacion)

    def aprobar(self):
        if self.calificacion>9:
            print('Aprobado')
            return
        print('Aplazado')

alumno1=Alumno('Ana', 8)
alumno1.mostrar()
alumno1.aprobar()
alumno2=Alumno('Francisco', 13)
alumno2.mostrar()
alumno2.aprobar()
