''' Consigna:
Hacer una función sonIguales() que reciba dos 
valores enteros, y evalúe si son iguales o si son 
diferentes, devolver True si es correcto o False en caso contrario.
'''


def sonIguales(valorA, valorB):
    if (valorA == valorB):
        return True
    else:
        return False


print(sonIguales(8,8)) # debería devolver True