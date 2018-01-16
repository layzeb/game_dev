# -*- coding: utf8 -*-
# Desenvolvido em MAR 2017
import random
random.seed()

rodadas = 0
acertos = 0

def menu():
	run = True
	
	while run:
		print("\t\tJOGO DO CARA OU COROA\n\n")
		play = input("Jogar ou Sair? [J/S]: ")
		if play == "J" or play == 'j':
			play_game()
		elif play == "S" or play == 's':
			print("Voce jogou", rodadas, "rodadas.")
			print("Voce acertou", acertos, "vez(es).")
			quit_game()
			run = False
		else:
			print("Opcao invalida, tente novamente.\n")
			continue

def quit_game():
	print("\nJogo desenvolvido por Layze Brandao")
	print("Obrigada por Jogar!")

def play_game():
	global rodadas
	global acertos
	
	print("Escolha um lado da moeda: ")
	p1 = int(input("Digite '1' para escolher Cara ou '2' para Coroa: "))
	if p1 != 1 and p1 != 2:
		print("Opcao invalida\n")
	else:
		coin = random.randint(1,2)
		rodadas += 1
		if p1 == coin:
			print("Acertou!\n")
			acertos += 1
			return 1
		else:
			print("Erooooou!\n")
			return 0
	
menu()
