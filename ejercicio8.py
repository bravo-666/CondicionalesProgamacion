'''
#Programa que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
#y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
#la edad es mayor o igual a dieciocho y el sexo es 'F'. 
#En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
#Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.
'''
n = int(input('Ingrese Nota: '))
e = int(input('Ingrese Edad: '))
s = str(input('Ingrese sexo F o M: ')).lower()

if n >= 5 and e >= 18 and s == 'f':
    print('Aceptada')
elif n >= 5 and e >= 18 and s == 'm':
    print('Posible')
else:
    print('No Aceptado')
