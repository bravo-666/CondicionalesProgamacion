'''
#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son ((100 alumnos o más, el costo por cada alumno es de 65 euros;)) 
#de ((50 a 99 alumnos, el costo es de 70 euros)), ((de 30 a 49, de 95 euros)), 
#y si son ((menos de 30, el costo de la renta del autobús es de 4000)) euros, 
#sin importar el número de alumnos. 
#Realice un programa que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje
'''
na = int(input('Numero de alumnos: '))
if na >= 100:
    print(f'El costo del autobus sera de {na * 65} euros')
elif na >= 50 and na <= 99:
    print(f'El costo del autobus sera de {na * 70} euros')
elif na >= 30 and na <= 49:
    print(f'El costo del autobus sera de {na * 95} euros')
elif na >= 0 and na <= 30:
    print('El costo del autobus sera de 4000 euros')