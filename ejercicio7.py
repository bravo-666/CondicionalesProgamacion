'''
# Realiza un programa que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
'''

a = int(input('Escribe un numero: '))
b = int(input('Escribe su potencia: '))


if b > 0:
    print(a ** b)
elif b == 0:
    print('1')
else:
    print(a ** abs(b))
