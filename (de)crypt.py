# -*- coding: utf-8 -*-
# Desenvolvido em MAR 2017

# Baseado no caesar cipher rot13


import string

def rot13(mess):
	cript = ""
	low_alfa = string.ascii_lowercase
	
	for i in mess:
		if i == " ":
			cript = cript + " "
		else:
			pos = low_alfa.find(i)
			if pos < 13:
				cript = cript + low_alfa[pos + 13]
			else:
				cript = cript + low_alfa[(pos + 13)%26]
	
	return cript

def decript(msg):
	alfa = string.ascii_lowercase
	transl = ""
	
	for i in msg:
		if i == " ":
			transl = transl + " "
		else:
			pos = alfa.find(i)
			transl = transl + alfa[pos-13]
	
	return transl

print('Bem-vindo ao (de)crypt!!!')
print('Escolha uma das opções abaixo, digitando o número correspondente: ')
print('''
[1] Criptografar Mensagem
[2] Descriptografar Mensagem''')

opcao = input()
if opcao == '1':
	print('Digite a mensagem a ser Criptografada sem pontuação e sem acentos ou cedilha: \n')
	tocrypt = input()
	print(rot13(tocrypt))
elif opcao == '2':
	print('Digite a mensagem a ser Descriptografada: \n')
	todecrypt = input()
	print(decript(todecrypt))
