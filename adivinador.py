# Ejercicio práctico
import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

número = random.randint(1, 10)
print('Bien, ' + miNombre + ', estoy pensando en un número entre 1 y 10.')

while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print('Tu estimación es muy baja.')
    
    if estimación > número:
        print('Tu estimación es muy alta.')
    
    if estimación == número:
        break

if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has acertado mi número en ' + intentosRealizados + ' intentos!')

if estimación != número:
    número = str(número)
    print('Pues no. El número en el que estaba pensando era el ' + número + '.')