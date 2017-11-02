# -*- coding: utf8 -*-
# Desenvolvido em MAR 2017

from random import seed, randint


tentativas = 0

def menu():

	while True:
		print("\t\tADIVINHE O NUMERO\n\n")
		play = input("Jogar ou Sair? [J/S]: ").lower()
		if play == 'j':
			play_game()
			if play_game == True:
				break
		elif play == 's':
			quit_game()
			break
		else:
			print("Opcao invalida, tente novamente.\n")
			continue
		
def quit_game():
	print("\nJogo desenvolvido por Layze Brandao")
	print("Obrigada por Jogar!")

def play_game():
	
	global tentativas
	num = randint(0, 100)
	
	while True:
		guess = int(input("Adivinhe um numero entre 0-99: \n"))
		if guess > 99 or guess < 0:
			print("Opcao invalida, tente novamente.\n")
			continue
		else:
			if guess == num:
				tentativas += 1
				print("Voce acertou em {} tentativas.\n".format(tentativas))
				break
			elif guess < num:
				print("Tente um numero maior.\n")
				tentativas += 1
				continue
			else:
				print("Tente um numero menor.\n")
				tentativas += 1
				continue
menu()
	
	
