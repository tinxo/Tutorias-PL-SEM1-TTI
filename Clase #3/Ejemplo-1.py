'''
Ejemplo de desarrollo de una clase
Escenario:
Se debe mantener la información correspondiente a los médicos de una clínica.
Es necesario guardar nombres y apellidos del profesional, nro. de celular,
especialidad y nro. de matrícula.
'''


class Medico:
    ''' Clase para registro de médicos. '''

    def __init__(self, apellidos, nombres, nroCelular, especialidad, nroMatricula):
        self.apellidos = apellidos
        self.nombres = nombres
        self.nroCelular = nroCelular
        self.especialidad = especialidad
        self.nroMatricula = nroMatricula

    def getApellidos(self):
        return self.apellidos

    def getNombres(self):
        return self.nombres

    def getNroMatricula(self):
        return self.nroMatricula

    def __str__(self):
        return f'{self.apellidos}, {self.nombres} - M.P. Nro.: {self.nroMatricula}'


# Generación de objetos de la clase
unMedico = Medico('Carter', 'John', '3765789876', 'Cirugia General', '4041')
print(unMedico)
print(f'El número de matricula es: {unMedico.getNroMatricula()}')
