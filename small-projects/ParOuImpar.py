# -*- coding: utf8 -*-
# Desenvolvido em MAR 2017

import random
random.seed()

p1win = 0
pcwin = 0
rodadas = 0
name = ""

def menu():
	global name
	run = True
	print("\t\tJOGO DO PAR OU ÍMPAR\n\n")
	print("\nEscolha um numero de 0 a 9 e duele contra a máquina!!\n")
	name = input("Digite seu nome: \n").strip()
	print("Bem-vindo, ", name)
	
	while run:	
		
		play = input("Jogar ou Sair? [J/S]: \n")
		if play == "S" or play == "s":
			estatisticas()
			sair()
			run = False
		elif play == "J" or play == "j":
			jogo()
		else:
			print("Opcao invalida. Digite 'J' para jogar ou 'S' para sair: \n")
			continue

def jogo():
	global p1win
	global pcwin
	global rodadas
	
	game = False
	while game == False:
		escolha = input("Par ou Impar? [P/I]: \n")
		if escolha != 'P' and escolha != 'p' and escolha != 'I' and escolha != 'i':
			print("Opcao invalida! Digite 'P' para escolher Par ou 'I' para escolher Impar\n")
		else:
			game = True
			p1 = int(input("Escolha um numero de 0 a 9: "))
			print("Seu numero: ", p1)
			pc = random.randrange(0,9)
			print("Computador: ", pc)
			result = p1 + pc
			print("Resultado: ", result)
			rodadas += 1
			if result % 2 == 0:
				if escolha == "p" or escolha == "P":
					print("Voce venceu!\n")
					p1win += 1
				else:
					print("Voce perdeu!\n")
					pcwin += 1
			else:
				if escolha == "i" or escolha == "I":
					print("Voce venceu!\n")
					p1win += 1
				else:
					print("Voce perdeu!\n")
					pcwin += 1

def estatisticas():
	global p1win
	global pcwin
	global rodadas
	global name
	
	print("Rodadas disputadas:", rodadas)
	print("\tPLACAR FINAL: ")
	print(name, p1win, " X ", pcwin, "Computador\n")
	
def sair():
	print("\n\nJogo desenvolvido por Layze Brandão")
	print("Obrigada por Jogar!")

menu()
	
