# Ejercicio práctico
import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

numero = random.randint(1, 10)
print('Bien, ' + miNombre + ', estoy pensando en un número entre 1 y 10.')

while intentosRealizados < 6:
    print('Intenta adivinar.')
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimación es muy baja.')
    
    if estimacion > numero:
        print('Tu estimación es muy alta.')
    
    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has acertado mi número en ' + intentosRealizados + ' intentos!')

if estimacion != numero:
    numero = str(numero)
    print('Pues no. El número en el que estaba pensando era el ' + numero + '.')
