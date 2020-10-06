# Practice exercise
import random

intentosRealizados = 0

print('¡Hi! Insert your name, please.')
miNombre = input()

número = random.randint(1, 10)
print('Nice, ' + miNombre + ', I am thinking of a number between 1 and 10.')

while intentosRealizados < 6:
    print('Try to guess.')
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print('Your estimate is too low.')
    
    if estimación > número:
        print('Your estimate is very high.')
    
    if estimación == número:
        break

if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Good job, ' + miNombre + '! ¡You guessed my number in ' + intentosRealizados + ' tries!')

if estimación != número:
    número = str(número)
    print('Incorrect. The number I was thinking of was ' + número)