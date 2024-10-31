'''
# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.
'''
u = str(input('Ingrese Usuario: ')).lower()
c = str(input('Ingrese Contrasena: ')).lowe()

if u == 'pepe' and c == 'jajaja':
    print('Has ingresado')
else:
    print('Acceso denegado')
    