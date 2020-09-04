'''
Ejercicio de ejemplo #2:
Se dispone de un diccionario con el espacio libre en su nube.
Se quiere generar una lista con los que han usado más del 80%
de su capacidad. Capacidad máxima = 10Gb.
'''


def capacidadMax(listadoUsuarios):
    listaExcedidos = []
    for user in listadoUsuarios.keys():
        if (listadoUsuarios[user] >= 8.0):
            # print(user)
            listaExcedidos.append(user)
    return listaExcedidos


print('Vamos a cargar los usuarios y su uso del espacio.')
usuarios = {}
for i in range(3):
    usuario = input('Ingrese el nombre del usuario: ')
    espacio = float(input('Ingrese el espacio usado en GB: '))
    usuarios[usuario] = espacio

# print(usuarios)
notificar = capacidadMax(usuarios)
print(f'Los usuarios a notificar son: {notificar}')
