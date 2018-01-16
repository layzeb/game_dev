# -*- coding: utf8 -*-
# Desenvolvido em OUT 2017

import pygame
from pygame.locals import *
import random
import sys, time


TELA = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Pysilisco')
FPS = 15


BRANCO = (255,255,255)
PRETO = (0,0,0)
VERDE = (0,155,0)
VERMELHO = (255,0,0)


CIMA = 'cima'
BAIXO = 'baixo'
DIREITA = 'direita'
ESQUERDA = 'esquerda'

pygame.init()

FPSCLOCK = pygame.time.Clock()

cabeca = [100,50]
cobraCoord = [[100,50],[90,50],[80,50]]
direcao = DIREITA

comida = [random.randrange(1, 72) * 10, random.randrange(1,46) *10]

pontos = 0

def gameOver():
	fonte = pygame.font.SysFont('monaco', 72)
	telaGameover = fonte.render('Game Over!', True, BRANCO)
	rectGameover = telaGameover.get_rect()
	rectGameover.midtop = (360,15)
	TELA.blit(telaGameover, rectGameover)

	mostraPontos()
	pygame.display.flip()
	time.sleep(2)
	pygame.quit()
	sys.exit()

def mostraPontos():
	fontePontos = pygame.font.SysFont('monaco', 24)
	telaPontos = fontePontos.render('Pontos: {}'.format(pontos), True, BRANCO)
	rectPontos = telaPontos.get_rect()
	rectPontos.midtop = (360,120)
	TELA.blit(telaPontos, rectPontos)


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			elif event.key == K_UP and direcao != BAIXO:
				direcao = CIMA
			elif event.key == K_DOWN and direcao != CIMA:
				direcao = BAIXO
			elif event.key == K_RIGHT and direcao != ESQUERDA:
				direcao = DIREITA
			elif event.key == K_LEFT and direcao != DIREITA:
				direcao = ESQUERDA

	TELA.fill(PRETO)

	if direcao == DIREITA:
		cabeca[0] += 10
	elif direcao == ESQUERDA:
		cabeca[0] -= 10
	elif direcao == CIMA:
		cabeca[1] -= 10
	elif direcao == BAIXO:
		cabeca[1] += 10

	cobraCoord.insert(0, list(cabeca))


	if cabeca[0] == comida[0] and cabeca[1] == comida[1]:
		comida = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
		pontos += 1
	else:
		cobraCoord.pop()


	for coord in cobraCoord:
		pygame.draw.rect(TELA, VERDE, pygame.Rect(coord[0],coord[1],10,10))


	pygame.draw.rect(TELA, VERMELHO, pygame.Rect(comida[0], comida[1], 10, 10))

	if cabeca[0] > 710 or cabeca[0] < 0 or cabeca[1] > 450 or cabeca[1] < 0:
		gameOver()


	for parteCorpo in cobraCoord[1:]:
		if cabeca[0] == parteCorpo[0] and cabeca[1] == parteCorpo[1]:
			gameOver()



	#mostraPontos()
	pygame.display.flip()
	FPSCLOCK.tick(FPS)


