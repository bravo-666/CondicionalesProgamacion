'''
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".
'''

n1 = int(input('Introduce tu Numero: '))

if n1>6 and n1<1:
    print('Error')
elif n1==1:
    print('El lado opuesto es el SEIS')
elif n1==2:
    print('El lado opuesto es el CINCO')
elif n1==3:
    print('El lado opuesto es el CUATRO')
elif n1==4:
    print('El lado opuesto es el TRES')
elif n1==5:
    print('El lado opuesto es el DOS')
elif n1==6:
    print('El lado opuesto es el UNO')
else:
    print('ERROR')
