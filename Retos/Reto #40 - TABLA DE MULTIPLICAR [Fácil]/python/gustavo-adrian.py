"""
Crea un programa que sea capaz de solicitarte un número y se
encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
  - Debe visualizarse qué operación se realiza y su resultado.
    Ej: 1 x 1 = 1
        1 x 2 = 2
        1 x 3 = 3
        ... 
"""


print('Tablas de multiplicar. Del 1 al 10.')
print('-'*40)


def tabla(n):
    lista = [e for e in range(1,11)]
    
    if 0<n<11:
        result = list(map(lambda m: m*n, lista))
        print(f'Tabla del {n}:')
        for i, x in enumerate(result):
            print(f'{i+1} x {n} = {x}')
    else:
        print('Debe ingresar un numero entre 1 y 10')
        tabla(int(input('Ingrese numero: ')))


tabla(int(input('Ingrese numero: ')))
        
