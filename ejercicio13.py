'''
#Realiza un programa que pida el dia de la semana (del 1 al 7) y escriba 
#el dia correspondiente. 
# Si introducimos otro número nos da un error.
'''

d = int(input('Introduce el numero del dia de la semana: '))

if d==1:
    print('Domingo')
elif d==2:
    print('Lunes')
elif d==3:
    print('Martes')
elif d==4:
    print('Mircoles')
elif d==5:
    print('Jueves')
elif d==6:
    print('Viernes')
elif d==7:
    print('Sabado')
else:    
    print('Error')
