print('Programa que lee dos nimeros ')
print('Nos dice cual es el mayor')
num1 = int(input('ingresa un numero: '))
num2 = int(input('Ingresa el segundo numero: '))
if num1 > num2:
    print(f'El {num1} es mayor')
elif num1 == num2:
    print(f'Los dos numeros son iguales')
else:
    print(f'El {num2} es mayor')
