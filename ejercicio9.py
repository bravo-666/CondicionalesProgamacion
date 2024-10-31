'''
#Programa que pida tres números y los muestre ordenados (de mayor a menor);
'''
n1 = int(input('Indroduce el primer numero: '))
n2 = int(input('Indroduce el segundo numero: '))
n3 = int(input('Indroduce el tercer numero: '))

if n1 > n2 > n3:
    print(n1, n2, n3)
elif n1 > n3 > n2:
    print(n1, n3< n2)
elif n2 > n1 > n3:
    print(n2, n1, n3)
elif n2 > n3> n1:
    print(n2, n3, n1)
elif n3 > n1 > n2:
    print(n3, n1, n2)
else:
    print(n3, n2, n1)