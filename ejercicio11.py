'''
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
'''
ll = float(input('Tiempo en minutos: '))
t = str(input('Ingrese timpo horiario Mañana o Tarde o el dia Domingo: ')).lower()

p1 = ll/100*15
p2 = ll/100*10
p3 = ll/100*3
#print(p1, p2, p3)

m1 = ll*1
m2 = ll*0.8
m3 = ll*0.7
m4 = ll*0.5
#print(m1, m2, m3, m4)

if ll>=0 and ll<=5 and t=='mañana':
    print(f'El costo de la llamada es {m1 + p1} euros')
elif ll>=0 and ll<=5 and t=='tarde':
    print(f'El costo de la llamada es {m1 + p2} euros')
elif ll>=0 and ll<=5 and t=='domingo':
    print(f'El costo de la llamada es {m1 + p3} euros')

elif ll>5 and ll<=8 and t=='mañana':
    print(f'El costo de la llamada es {m2 + p1} euros')
elif ll>5 and ll<=8 and t=='tarde':
    print(f'El costo de la llamada es {m2 + p2} euros')
elif ll>5 and ll<=8 and t=='domingo':
    print(f'El costo de la llamada es {m2 + p3} euros')

elif ll>8 and ll<=10 and t=='mañana':
    print(f'El costo de la llamada es {m3 + p1} euros')
elif ll>8 and ll<=10 and t=='tarde':
    print(f'El costo de la llamada es {m3 + p2} euros')
elif ll>8 and ll<=10 and t=='domingo':
    print(f'El costo de la llamada es {m3 + p3} euros')

elif ll>10 and t=='mañana':
    print(f'El costo de la llamada es {m4 + p1} euros')
elif ll>10 and  t=='tarde':
    print(f'El costo de la llamada es {m4 + p2} euros')
elif ll>10 and t=='domingo':
    print(f'El costo de la llamada es {m4 + p3} euros')