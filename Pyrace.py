# PYRACE V1.0
# Início de desenvolvimento: 2017 NOV 07
# Desenvolvedora: Layze Brandão
# Python 3.4.3


# -*- coding: utf8 -*-

from random import randrange, sample
from time import sleep

print('-='*15)
print('WELCOME TO PY-RACE'.center(30))
print('-='*15)

print('''
__
.-'--`-._
'-O---O--'
''')

print('\n\nEnfrente outro jogador percorrendo um caminho numerado de 1 a 50.')
print('Jogue o dado para determinar sua nova posição.')
print('Encontre blocos com bônus que te ajudarão a completar o caminho...')
print('ou blocos com desvantagens que te atrasarão.')
print('Quem vai ganhar? A sorte está lançada!!\n\n')

print('Insira o nome dos jogadores: \n')
p1 = input('Player 1: \n').upper()
p2 = input('Player 2: \n').upper()

print('\n'*100)

print('-='*5,end='')
print(' {} VS. {} '.format(p1,p2),end='')
print('-='*5)

# inicializando 

p1_pos = 0      # posição do player 1
p2_pos = 0      # posição do player 2
dado = 0        # dado
vez = 1         # turno de cada jogador
required_to_win = 0     # pontos necessários para vencer


# criando e colocando as posições da lista de bônus

bonuspos = sample(range(2,50), 5)   # números aleatórios únicos no intervalo 2 a 50

# criando e colocando as posições da lista de desvantagens
losspos = []

while len(losspos) < 5:
    num = randrange(2,50)
    if num not in bonuspos and num not in losspos:  # checa se os números são únicos
        losspos.append(num)

print('Posições de rodada extra: {}.'.format(sorted(bonuspos)))
print('Posições de perda de rodada: {}.'.format(sorted(losspos)))


def rolaDados():
    
    '''Função que retorna um valor para o dado, de forma aleatória'''
    
    global dado
    
    rolar = input('Jogue o dado [pressione ENTER]')
    print('Rolando dado...')
    sleep(3)
    dado = randrange(1,7)
    print('Resultado do dado: {}'.format(dado))
    return dado

# inicializando variáveis lógicas para controle do turno em que há perda da vez de jogar

p1_loss = False 
p2_loss = False

while p1_pos <= 50 or p2_pos <= 50:     # enquanto nenhum dos jogadores alcança a chegada
    
    if vez % 2 == 1:    # se o valor de VEZ for ímpar, joga o player 1
        
        if p1_loss == True:     # checa se o player perdeu a vez
            vez += 1            # incrementa VEZ
            p1_loss = False     # muda de volta a variável para o estado inicial
            continue            # reinicia o loop sem rolar o dado
        
        print('\nVez de {}: '.format(p1))
        
        rolaDados()     # chama a função que rola os dados
        
        required_to_win = 50 - p1_pos   # calcula quantos pontos faltam para a chegada
        
        # se a qtd de pontos p/ a chegada coincidir com o valor do dado: jogador vence
        
        if required_to_win  == dado:    
            p1_pos += dado
            print('Posição de {}: {}'.format(p1, p1_pos))
            print('\n{} VENCEU!!'.format(p1))
            break
        else:  
            if p1_pos + dado < 50:  # se ainda n venceu e a nova posição < q o limite
                p1_pos += dado      # a nova posição será a antiga + valor do dado
        
        print('Posição de {}: {}'.format(p1, p1_pos))
        
        
        if p1_pos in bonuspos:  # se a nova posição cair num bônus, reinicia o loop
            print('Rodada bônus! Jogue mais uma vez!')
            continue
        elif p1_pos in losspos: # se a nova posição cair numa perda, a variável lógica muda
            print('Ah não! Fica uma rodada sem jogar!')
            p1_loss = True
        
        vez += 1    # muda a vez para o próximo jogador atuar
    
    else:
        
        if p2_loss == True:
            vez += 1
            p2_loss = False
            continue
        
        print('\nVez de {}: '.format(p2))
                
        rolaDados()
        required_to_win = 50 - p2_pos
        
        if required_to_win  == dado:
            p2_pos += dado
            print('Posição de {}: {}'.format(p2, p2_pos))
            print('\n{} VENCEU!!'.format(p2))
            break
        else:
            if p2_pos + dado < 50:
                p2_pos += dado
        
        print('Posição de {}: {}'.format(p2, p2_pos))
        
        if p2_pos in bonuspos:
            print('Rodada bônus! Jogue mais uma vez!')
            continue
        elif p2_pos in losspos:
            print('Ah não! Fica uma rodada sem jogar!')
            p2_loss = True
        
        vez += 1
