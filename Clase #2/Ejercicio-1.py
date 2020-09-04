'''
Ejercicio de ejemplo #1:
Se tiene un listado de DNI de pasajeros de un vuelo.
Se dispone de un listado de DNI de personas no aptas para viajar.
Se espera indicar si existe algún pasajero que no pueda viajar.
En caso de haberlo, informar la cantidad.
Además de informar por cada uno su condición.
'''


def validarPasajeros(lista, bloqueados):
    resultado = 0
    for persona in lista:
        if (persona in bloqueados):
            # DNI en lista negra -- no vuela
            resultado += 1
            print(f'El DNI {persona} no puede volar.')
        else:
            print(f'El DNI {persona} puede viajar normalmente.')
    return resultado


pasajeros = ['12345678', '23456789', '345678901', '456789012', '567890123', '678901234']
listaNegra = ['23456789', '567890123', '90123456']
noViajan = validarPasajeros(pasajeros, listaNegra)
if (noViajan > 0):
    print(f'Revisar listado previo, hay {noViajan}  pasajero/s que no pueden viajar.')
else:
    print('Luz verde, todos ok.')
