# Practice exercise
import random

intentosRealizados = 0

print('¡Hi! Insert your name, please.')
miNombre = input()

numero = random.randint(1, 10)
print('Nice, ' + miNombre + ', I am thinking of a number between 1 and 10.')

while intentosRealizados < 6:
    print('Try to guess.')
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Your estimate is too low.')
    
    if estimacion > numero:
        print('Your estimate is very high.')
    
    if estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Good job, ' + miNombre + '! ¡You guessed my number in ' + intentosRealizados + ' tries!')

if estimacion != numero:
    numero = str(numero)
    print('Incorrect. The number I was thinking of was ' + numero)
    