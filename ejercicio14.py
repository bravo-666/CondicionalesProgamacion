'''
#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
'''

m = int(input('Introduce el mes en numero: '))

if m==1:
    print('El mes es ENERO')
elif m==2:
    print('El mes es FEBREO')
elif m==3:
    print('El mes es MARZO')
elif m==4:
    print('El mes es ABRIL')
elif m==5:
    print('El mes es MAYO')
elif m==6:
    print('El mes es JUNIO')
elif m==7:
    print('El mes es JULIO')
elif m==8:
    print('El mes es AGOSTO')
elif m==9:
    print('El mes es SEPTIEMBRE')
elif m==10:
    print('El mes es OCTUBRE')
elif m==11:
    print('El mes es NOVIEMBRE')
elif m==12:
    print('El mes es DICIEMBRE')
else:
    print('ERROR')
