#Programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
import random
x = random.randint(0,5)
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' *20)
jogador =int(input('Em que número pensei?'))
if jogador == x:
    print('Parabéns, você venceu')
else:
    print('Você perdeu, tente outra vez!')
print('Pensei no número...{}'.format(x))