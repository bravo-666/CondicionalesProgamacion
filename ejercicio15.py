'''
# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta
'''
j1 = str(input('Primer jugador, elige piedra, papel o tijera: ')).lower()
j2 = str(input('Segundo jugador, elige piedra, papel o tijera: ')).lower()

if j1 == j2:
    print('Jugadores empatados')
elif (j1 == 'piedra' and j2 == 'tijera') or \
     (j1 == 'tijera' and j2 == 'papel') or \
     (j1 == 'papel' and j2 == 'piedra'):
    print('El jugador 2 GANA')
elif (j2 == 'piedra' and j1 == 'tijera') or \
     (j2 == 'tijera' and j1 == 'papel') or \
     (j2 == 'papel' and j1 == 'piedra'):
    print('El jugador 2 GANAS')
else:
    print('Opcion incorrecta')
