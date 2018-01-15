# -*- coding: utf8 -*-
# v3.1

from random import seed, sample, choice

seed()

pontos = rodadas = 0
wordlist = chaves = []
categoria = nivel = aleat = ""


def menu():
    """Funcao contendo o menu do jogo."""
    global nivel

    print("\t\t\tANAGRAMAS: UNSCRUMBLED v3.0\n")
    print("As letras estão embaralhadas. Consegue desvendar as palavras?\n")
    print("ESCOLHA O NIVEL DE DIFICULDADE DIGITANDO O NUMERO CORRESPONDENTE: \n")
    print("1 - Iniciante / Soletrando")
    print("2 - Veterano / Nota mil no ENEM")
    print("3 - Gênio / Eminem rap god")
    nivel = input()
    regras()
    play = input("Vamos jogar? [S/N]: \n").lower()
    if play == 's':
        play_game()
    elif play == 'n':
        quit_game()
    else:
        print("Opção inválida, tente novamente.\n")
        menu()


def regras():
    global nivel

    def regras_nv1():
        print("Cada palavra correta na primeira tentativa vale 3 pontos.")
        print("Caso a primeira tentativa esteja incorreta, voce terá uma dica.")
        print("Cada acerto na segunda tentativa vale 1 ponto.")
        print("Em caso de dois erros na mesma palavra, nenhum ponto será computado.")

    def regras_nv2():
        print("Cada palavra correta na primeira tentativa vale 5 pontos.")
        print("Caso a primeira tentativa esteja incorreta, voce terá uma dica.")
        print("Cada acerto na segunda tentativa vale 3 pontos.")
        print("Em caso de dois erros na mesma palavra, será computado 1 ponto.")

    def regras_nv3():
        print("Cada palavra correta vale 10 pontos.")
        print("Neste nivel você não terá dica.")
        print("Em caso de erro, nenhum ponto será computado.")

    print("REGRAS: \n")
    if nivel == "1":
        regras_nv1()
    elif nivel == "2":
        regras_nv2()
    elif nivel == "3":
        regras_nv3()
    else:
        print("Opção inválida, tente novamente.\n")
        menu()
    print("Todas as palavras devem ser digitadas sem acentos ou cedilha.")
    print("BOA SORTE!")


def choose_cat():
    """Uma funcao que mostra as categorias do jogo e solicita uma escolha dentre elas. Tambem estabelece as dicas das 
    palavras listadas """

    global categoria

    print("\nESCOLHA UMA DAS CATEGORIAS ABAIXO DIGITANDO O NUMERO CORRESPONDENTE: \n")
    print("1 - Natureza\n")
    print("2 - Corpo humano\n")
    print("3 - Comida\n")
    categoria = input()
    listas_palavras()


def listas_palavras():
    global wordlist, categoria, aleat, nivel, chaves

    if nivel == "1" and categoria == "1":
        wordlist = {"planta": "relva", "solo": "chao", "oceano": "maritmo", "baleia": "animal", "flor": "petala",
                    "agua": "liquido", "areia": "terra", "ilha": "ínsula", "grama": "capim", "frio": "temperatura"}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "1" and categoria == "2":
        wordlist = {"pele": "derme", "dente": "boca", "tendao": "ligamento", "intestino": "abdomen", "unha": "dedos",
                    "nariz": "olfato", "pulmao": "respiracao", "torax": "peito", "veia": "vaso", "testa": "fronte",
                    "pulso": "carpo", "quadril": "cintura"}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "1" and categoria == "3":
        wordlist = {"macarrao": "massa", "chocolate": "doce", "melancia": "fruta", "bisteca": "churrasco",
                    "sorvete": "sobremesa"}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "2" and categoria == "1":
        wordlist = {"planta": "relva", "solo": "chao", "oceano": "maritmo", "baleia": "animal", "flor": "petala",
                    "agua": "liquido", "areia": "terra", "ilha": "ínsula", "grama": "capim", "frio": "temperatura",
                    "estrela": "ceu", "girassol": "flor", "represa": "barragem", "deserto": "despovoado",
                    "inseto": "bicho", "neblina": "nevoa", "nevasca": "tempestade", "laguna": "lago",
                    "pantano": "atoleiro"}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "2" and categoria == "2":
        wordlist = {"pele": "derme", "dente": "boca", "tendao": "ligamento", "intestino": "abdomen", "unha": "dedos",
                    "nariz": "olfato", "pulmao": "respiracao", "torax": "peito", "veia": "vaso", "testa": "fronte",
                    "pulso": "carpo", "quadril": "cintura", "coracao": "cardiaco", "pupila": "olho", "bexiga": "urina",
                    "gengiva": "boca", "mamilo": "peito", "laringe": "garganta", "saliva": "cuspe", "ouvido": "orelha"}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "2" and categoria == "3":
        wordlist = {"macarrao": "massa", "chocolate": "doce", "melancia": "fruta", "bisteca": "churrasco",
                    "sorvete": "sobremesa"}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "3" and categoria == "1":
        wordlist = {"planta": 'oi', "solo": 'oi', "oceano": 'oi', "baleia": 'oi', "flor": 'oi', "agua": 'oi',
                    "areia": 'oi', "ilha": 'oi', "grama": 'oi', "frio": 'oi', "estrela": 'oi', "girassol": 'oi',
                    "represa": 'oi', "deserto": 'oi', "inseto": 'oi', "neblina": 'oi', "nevasca": 'oi', "laguna": 'oi',
                    "pantano": 'oi', "biodiversidade": 'oi', "reflorestamento": 'oi', "silvestre": 'oi',
                    "correnteza": 'oi', "relampago": 'oi', "penisula": 'oi', "cordilheira": 'oi', "desfiladeiro": 'oi',
                    "afluente": 'oi'}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "3" and categoria == "2":
        wordlist = {"derme": 'a', "boca": 'a', "ligamento": 'a', "abdomen": 'a', "dedos": 'a', "olfato": 'a',
                    "respiracao": 'a', "peito": 'a', "vaso": 'a', "rosto": 'a', "carpo": 'a', "cintura": 'a',
                    "cardiaco": 'a', "olho": 'a', "urina": 'a', "boca": 'a', "peito": 'a', "garganta": 'a',
                    "cuspe": 'a', "orelha": 'a', "vesicula": 'a', "estomago": 'a', "cotovelo": 'a', "prostata": 'a',
                    "antebraco": 'a', "cerebelo": 'a', "clavicula": 'a'}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)


    elif nivel == "3" and categoria == "3":
        wordlist = {"macarrao": 'q', "chocolate": 'q', "melancia": 'q', "bisteca": 'q', "sorvete": 'q'}
        chaves = list(wordlist.keys())
        aleat = choice(chaves)

    else:
        print("Categoria inexistente, tente novamente.")
        choose_cat()


def shuffle(palavra):
    """Funcao que recebe como argumento uma string para embaralhar os caracteres."""

    messed = ''.join(sample(palavra, len(palavra)))
    return messed


def play_game():
    global pontos, wordlist, rodadas, aleat, nivel, chaves

    while True:
        rodadas += 1
        choose_cat()
        print("\nQue palavra é essa?: " + shuffle(aleat) + "\n")
        p1 = input().lower()
        pos = chaves.index(aleat)
        if p1 == chaves[pos]:
            print("\nAcertou!")
            if nivel == "1":
                pontos += 3
            elif nivel == "2":
                pontos += 5
            else:
                pontos += 10
        else:
            if nivel == "3":
                print("Erroooooou! *Faustão face appears*\nA palavra correta era", chaves[pos], "\n")
            else:
                print("Dica: " + wordlist.get(aleat))
                p1 = input()
                if p1 == chaves[pos]:
                    print("\nAcertou!")
                    if nivel == "1":
                        pontos += 1
                    else:
                        pontos += 3
                else:
                    print("Erroooooou! *Faustão face appears*\nA palavra correta era", chaves[pos], "\n")

        again = input("\nPara continuar, pressione qualquer tecla. Para sair, digite 'N'. \n").lower()
        if again == 'n':
            break
        else:
            continue
    placar()


def placar():
    global pontos, rodadas, nivel

    print("\n\tPLACAR FINAL: \n")
    print("Você tentou adivinhar", rodadas, "palavra(s) e fez", pontos, "pontos")
    if nivel == "1":
        stat = (pontos * 100) / (rodadas * 3)
    elif nivel == "2":
        stat = (pontos * 100) / (rodadas * 5)
    else:
        stat = (pontos * 100) / (rodadas * 10)

    print("Seu aproveitamento foi de %.2f" % stat, "%")


def quit_game():
    print("Obrigada por Jogar!")


menu()
