# -*- coding: utf-8 -*-

import re as regex
import random


def main():
    repetir = True
    while repetir:
        qtdjogos = get_int_input("Quantos jogos deseja realizar?", 1)
        qtdnumeros = get_int_input("Quantos numeros deseja marcar em cada jogo?", 6)

        no_formato = False

        intervalo = None

        while not no_formato:
            mensagem = '''
Insira o intervalo de números no qual o jogo deverá ser feito.
Por exemplo, "1,60" (sem as aspas) gerará números que vão de 1 a 60.
Insira o valor desejado:'''

            intervalo = get_string_input(mensagem, "1,60")

            if regex.search('[0-9]+,[0-9]+', intervalo):
                no_formato = True
                intervalo = intervalo.split(',')
            else:
                print("Por favor, insira no formato '<número>,<número>' (sem as aspas).")


        jogos = []

        for i in range(qtdjogos):
            jogo = []
            for j in range(qtdnumeros):
                while True:
                    numero = random.randint(int(intervalo[0]), int(intervalo[1]))

                    if numero not in jogo:
                        jogo.append(numero)
                        break
            jogos.append(jogo)

        print("Seus " + str(len(jogos)) + " foram:")
        for jogo in jogos:
            jogo.sort()
            print(jogo)
        
        opcao = get_string_input("Deseja repetir? [s/n]", "n")

        if opcao.lower() == 'n':
            repetir = False
            



#aux functions
def get_int_input (message, default_value):
    try:
        return int(input(message + " [Default " + str(default_value) + "] "))
    except ValueError:
        return default_value

def get_string_input (message, default_value):
    try:
        string = str(input(message + " [Default " + str(default_value) + "] "))
        return string if string != "" else default_value
    except ValueError:
        return default_value

main()
