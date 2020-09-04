# Ejemplo para el desarrollo del Tema 1

apellidos = []
for i in range(4):
    ap = input('Ingrese un apellido: ')
    apellidos.append(ap)

print(f'El primer apellido es: {apellidos[0]}')

apellidos.insert(3, 'd')

print('Contenido de la lista:')
print(apellidos)
