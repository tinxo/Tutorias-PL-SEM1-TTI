'''
Ejemplo de desarrollo de una clase
Escenario:
Un sistema de gestión de congresos requiere una clase "Trabajo" para gestionar
los trabajos que se presentan para evaluación. Por cada trabajo se registran:
titulo, área temática a la que pertenece (A1, A2, A3) y estado (resultado de
evaluación); en el trabajo se registran también nombre y apellido del autor
y su correo electrónico.
Se pide un método de la clase que reciba las tres calificaciones numéricas
de evaluadores (del 1 al 10) y determine si el estado del trabajo debe ser: 
"Aceptado" (8 - 10),
"Aceptado con observaciones" (4 - 8),
"Rechazado" (0 - 4)
'''


class Trabajo:
    ''' Clase para los trabajos de un congreso.'''

    def __init__(self, titulo, areaTematica, apellidoAutor, nombreAutor, emailAutor, estado = 'Nuevo'):
        self.titulo = titulo
        self.areaTematica = areaTematica
        self.estado = estado
        self.apellidoAutor = apellidoAutor
        self.nombreAutor = nombreAutor
        self.emailAutor = emailAutor

    def getTitulo(self):
        return self.titulo

    def getEstado(self):
        return self.estado

    # TODO: hacer los otros métodos get + __str__

    def evaluacion(self, notas):
        promedio = 0
        for unaNota in notas:
            promedio += unaNota
        promedio /= len(notas)
        # Obtener la evaluación en función del promedio
        '''
        "Aceptado" (8 - 10),
        "Aceptado con observaciones" (4 - 8),
        "Rechazado" (0 - 4)
        '''
        if (promedio >= 8):
            self.estado = 'Aprobado'
        elif (promedio >= 4 and promedio < 8):
            self.estado = 'Aprobado con obs.'
        elif (promedio > 0 and promedio < 4):
            self.estado = 'Rechazado'


# Probar la generación de un trabajo y su evaluación
unTrabajo = Trabajo('Trabajo1', 'A1', 'Fulanito', 'Cosme', 'fulanito@fox.com')
print(f'El trabajo: {unTrabajo.getTitulo()} - Tiene un estado: {unTrabajo.getEstado()}')
calificaciones = [2, 1, 7]
unTrabajo.evaluacion(calificaciones)  # Aprobado
print(f'El trabajo: {unTrabajo.getTitulo()} - Tiene un estado: {unTrabajo.getEstado()}')
