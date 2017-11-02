# -*- coding: utf8 -*-
# Desenvolvido em JUN 2017

import time
from datetime import date

now = date.today()
dia = mes = ano = 0
signo = nasc = ''

def main():
	
	while True:
		print('='*50)
		print('\t\t   HORÓSCOPO')
		print('='*50)
		print('\n\n')
		nasc = input('Digite sua data de nascimento no formato DD/MM/AAAA: ')
		data_conv(nasc)
		if not isValid(nasc):
			continue
		horoscopo(nasc)
		caracteristicas_signo(signo)
		print('\nSua idade é {} anos.\n'.format(idade(nasc)))
		niver(nasc)
		break

def data_conv(data):
	global dia, mes, ano
	
	data = data.split('/')
	dia = int(data[0])
	mes = int(data[1])
	ano = int(data[2])

def isValid(date):
	global dia, mes, ano
	
	if dia <= 0 or dia > 31 or mes <= 0 or mes > 12 or ano > now.year:
		print('Data inválida.\n\n')
		return False
	elif mes == 2 and dia > 29:
		print('Data inválida.\n\n')
		return False
	else:
		return True

def horoscopo(data_nascimento):
	global dia, mes, signo
	
	if (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
		signo = 'Aquário'
	elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
		signo = 'Peixes'
	elif (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
		signo = 'Áries'
	elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
		signo = 'Touro'
	elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
		signo = 'Gêmeos'
	elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
		signo = 'Câncer'
	elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
		signo = 'Leão'
	elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
		signo = 'Virgem'
	elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
		signo = 'Libra'
	elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
		signo = 'Escorpião'
	elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
		signo = 'Sagitário'
	else:
		signo = 'Capricórnio'
	
	print('\nSeu signo é {}\n'.format(signo))
	
def caracteristicas_signo(um_signo):
	
	global signo
	
	desc_signos = { 'Aquário': 'Os aquarianos são tímidos e quietos, mas por outro lado eles podem ser excêntricos e energéticos. No entanto, em ambos os casos, eles são profundos pensadores e pessoas altamente intelectuais que gostam de ajudar os outros. Eles são capazes de enxergar sem preconceitos, em ambos os lados, o que os torna pessoas que facilmente resolvem problemas.',
			   'Peixes': 'Piscianos são muito simpáticos, então eles muitas vezes se encontram na companhia de pessoas muito diferentes. São altruístas, estão sempre dispostos a ajudar os outros, sem esperar receber nada em troca. Peixes é um signo de água e, dessa forma, este signo do zodíaco é caracterizado por empatia e capacidade emocional expressa.',
			   'Áries': 'Como o primeiro signo do zodíaco, a presença de Áries quase sempre marca o início de algo enérgico e turbulento. Estas pessoas estão continuamente à procura de dinâmica, velocidade e competição. Elas estão sempre em primeiro lugar em tudo - do trabalho a encontros sociais.',
			   'Touro': 'Poderoso e confiável, Touro é o primeiro quando se trata de colher os frutos do seu trabalho. Eles adoram tudo o que é bom e belo, e eles vivem muitas vezes cercados por prazeres materiais. As pessoas nascidas sob o signo de Touro são muito sensuais e táteis.',
			   'Gêmeos': 'Expressivo e de raciocínio rápido, Gêmeos representa dois lados diferentes da mesma personalidade e você nunca vai ter certeza de com quem você está falando. Gêmeos pode ser sociável, comunicativo e pronto para se divertir, entretanto, por outro lado, pode ser muito sério, pensativo, inquieto e indeciso.',
			   'Câncer': 'Profundamente intuitivo e sentimental, o canceriano pode ser um dos signos do zodíaco mais desafiadores para entender. Câncer é muito emocional e sensível, e se preocupa com a família e a casa. É simpático e muito apegado às pessoas que o cercam.',
			   'Leão': 'As pessoas nascidas sob o signo de Leão são líderes natos. Eles são dramáticos, criativos, autoconfiantes, dominantes e extremamente difíceis de resistir. Eles podem conseguir qualquer coisa que queiram, seja no trabalho ou no tempo gasto com a família e amigos.',
			   'Virgem': 'Os virginianos estão sempre prestando atenção nos menores detalhes e seu profundo senso de humanidade faz com que seja um dos signos mais cuidadosos do zodíaco. Sua abordagem metódica de vida garante que nada é deixado ao acaso.',
	           'Libra': 'As pessoas nascidas sob o signo de Libra são pacíficas e justas, e odeiam ficar sozinhas. A parceria é muito importante para os librianos, e com a sua mentalidade vitoriosa e cooperação, eles não conseguem ficar sozinhos.', 
	           'Escorpião': 'Os nascidos em Escorpião são pessoas apaixonadas e assertivas. Eles são determinados e decisivos, e pesquisam até encontrar a verdade. O Escorpião é um grande líder, sempre consciente das situações e também se destaca na engenhosidade.', 
	           'Sagitário': 'Curioso e energético, Sagitário é um dos maiores viajantes entre todos os signos do zodíaco. Sua mente aberta e visão filosófica os motiva a passear ao redor do mundo em busca do sentido da vida. Sagitário é extrovertido, otimista e entusiasta, e gosta de mudanças.', 
	           'Capricórnio': 'Quando se trata de profissionalismo e valores tradicionais, Capricórnio é o primeiro. Capricórnio é prático e é considerado como o signo mais sério do zodíaco, possuindo uma independência que permite progressos significativos tanto no nível pessoal quanto nos negócios.'}
	print(desc_signos.get(signo))

def idade(nascimento):
	if mes < now.month:
		age = now.year - ano
	elif mes == now.month:
		if dia < now.day:
			age = now.year - ano
		else:
			age = now.year - ano - 1
	else:
		age = now.year - ano - 1
	return age

def niver(day_nascimento):
	global dia, mes
	
	day_nascimento = date(day=dia, month=mes, year=now.year)
	day_now = date(day=now.day, month=now.month, year=now.year)
	
	cont_dias = abs((day_now - day_nascimento).days)
	
	if (day_now - day_nascimento).days > 0:
		print('Seu aniversário foi há {} dias.'.format(cont_dias))
	elif (day_now - day_nascimento).days < 0:
		print('Seu aniversário será daqui há {} dias.'.format(cont_dias))
	else:
		print('Parabéns! Hoje é seu aniversário!!!\n')

main()
