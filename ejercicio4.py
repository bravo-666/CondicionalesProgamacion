'''
# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.
'''
n1 = int(input('Escribe el primer numero: '))
n2 = int(input('Escribe el segundo numero: '))

if n2==0:
    print('#No se puede hacer esta operacion')
else:
    print(f'El resultado es: {n1/n2}')
