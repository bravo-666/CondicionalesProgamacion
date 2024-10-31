'''
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
'''
e = str(input('Escribe: '))
if (e.isupper()):
    print('El texto esta en mayusculas')
else:
    print('El texto no tiene mayusculas')