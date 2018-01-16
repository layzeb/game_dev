# -*- coding: utf8 -*-

from time import sleep
from random import choice


def main():

    print('-='*10)
    print('MAD LIBS RPG'.center(20))
    print('-='*10)
    print('Construa sua história de um jeito divertido!')
    sleep(5)


main()

heroi_list = ['Galante', 'Supergalático', 'Angelical', 'Guardião']
vilao_list = ['Zumbi', 'Esquecido', 'do Submundo', 'Pistoleiro', 'Saltitante']
quebra_list = ['quebrou', 'rachou', 'se desintegrou', 'pegou fogo','peidou']
defeat_list = ['espaço sideral', 'Vazio', 'inferno', 'mundo dos teletubbies']
heroi_adj = choice(heroi_list)
vilao_adj = choice(vilao_list)
quebra = choice(quebra_list)
defeat = choice(defeat_list)


heroi = input('Digite um substantivo comum masculino no singular. Ex: caderno, monitor.\n').capitalize()
vilao = input('Digite um substantivo comum masculino no singular. Ex: chocolate, sapato.\n').capitalize()
cidade = input('Digite um nome de lugar: \n')
habitantes = input('Digite um substantivo masculino plural. Ex: robôs, macacos. \n')
adj1 = input('Digite um adjetivo no plural. Ex: cansados, valentes. \n')
adj2 = input('Digite um adjetivo no plural. Ex: assustados, alegres. \n')
adj3 = input('Digite um adjetivo masculino no singular. Ex: estranho, maluco. \n')
arma = input('Digite um substantivo feminino no singular. Ex: Porta, cadeira. \n')
ataque = input('Digite um verbo no passado. Ex: comeu, trabalhou. \n')
corpo = input('Digite uma parte do corpo no singular. \n')
equip = input('Digite um substantivo comum masculino no singular. Ex: carro, poste \n')
corpo2 = input('Digite uma parte do corpo no masculino singular. Ex: olho, cabelo. \n')
adj4 = input('Digite um adjetivo masculino no singular. Ex: estranho, maluco. \n')
wingman = input('Digite um substantivo comum masculino no singular. Ex: carro, poste \n').capitalize()
obj = input('Digite um substantivo comum no plural. Ex: pedras, fios. \n')
verbo = input('Digite um verbo no infinitivo. Ex: comer, pular, sair. \n')

print('\n'*100)


print('-='*40)
print('O incrível {} {} vs. O Maligno {} {}.'.center(70).format(heroi, heroi_adj, vilao,vilao_adj))
print('-='*40)
sleep(3)
print('Era uma vez...')
sleep(2)
print('Havia uma pequena cidade chamada {}. Os {} que viviam lá estavam {} com suas vidas.'.format(cidade.capitalize(),habitantes,adj1))
sleep(7)
print('Um dia, tudo mudou!! Um gigante {} invadiu a cidade e tentou comer todos os {}.'.format(vilao,habitantes))
sleep(7)
print('Eles ficaram {} quando viram o {} e não sabiam o que fazer.'.format(adj2,vilao))
sleep(7)
print('Então, os {} invocaram o herói mais {} da cidade de {}: O {} {}!!'.format(habitantes,adj3,cidade,heroi_adj,heroi.capitalize()))
sleep(7)
print('Quando o {} {} viu o {} {}, instantaneamente sabia o que fazer.'.format(heroi_adj,heroi,vilao_adj,vilao))
sleep(7)
print('O {} agarrou uma gigantesca {} e {} o {} no(a) {} com ela!!!'.format(heroi,arma,ataque,vilao,corpo))
sleep(7)
print('Mas a {} {} quando ele {} o {}, que não sofreu nenhum arranhão.'.format(arma,quebra,ataque,vilao))
sleep(7)
print('Então o {} foi até os limites da cidade, encontrou um {}, voou até o {} e arremessou o {} no(a) {} dele.'.format(heroi,equip,vilao,equip,corpo2))
sleep(7)
print('Mas o {} {} também.'.format(equip,quebra))
sleep(3)
print('Nesse momento, mesmo {} {} estava {}. Então ele ligou para um companheiro de confiança: {} {}'.format(heroi,heroi_adj,adj4,wingman,choice(heroi_list)))
sleep(7)
print('Felizmente para o {} e os {} de {}, {} já havia encontrado o {} e sabia exatamente o que fazer.'.format(heroi,habitantes,cidade,wingman,vilao))
sleep(7)
print('{} modelou uma arma feita de {}, algo que o {} ficou com medo'.format(wingman,obj,vilao))
sleep(5)
print('Quando o {} viu a nova arma, tentou destrui-la.'.format(vilao))
sleep(5)
print('Aproveitando a distração do {}, {} deu um sinal para o {} {}, que então pegou o {} e o atirou para o {}, onde nunca mais poderia prejudicar alguém novamente.'.format(vilao,wingman,heroi,heroi_adj,vilao,defeat))
sleep(10)
print('Os {} de {} começaram a {} de alegria quando o {} foi derrotado.'.format(habitantes,cidade,verbo,vilao))
sleep(5)
print('E todos agradeceram ao {} {} e seu amigo {}'.format(heroi,heroi_adj,wingman))
sleep(5)
print('Fim.')





