# Ejemplo correspondiente al Tema 4 de la Clase #1
'''
for i in range(3):
    print(i)
    nombre = input('Ingrese su nombre: ')
    temperatura = float(input('Ingrese su temperatura: '))
    if (temperatura >= 37.5):
        # caso sospechoso de covid19
        print(f'Hola {nombre}, dado que su temeperatura es de {temperatura}° ud. es un caso sospechoso de covid 19')
    else:
        # caso "no sospechoso"
        print(f'Hola {nombre}, bienvenido.')
'''
'''
# Ejemplo while

tempCasa = int(input('Ingrese la temperatura del ambiente: ')) # quiero bajar la temp de la casa a 24°
while (tempCasa > 24):
    print(f'Se debe ajustar la temperatura, actual = {tempCasa}')
    tempCasa = tempCasa - 1

print(f'Temperatura final {tempCasa}')
'''


def chequeoTemp(temperatura):
    if (temperatura >= 37.5):
        # devuelve True si es un caso sospechoso        
        return True
    else:
        # devuelve False en caso contrario
        return False


tempUsuario = float(input('Ingrese su temperatura: '))
if (chequeoTemp(tempUsuario)):
    print('Caso sospechoso')
else:
    print('Caso no sospechoso')
