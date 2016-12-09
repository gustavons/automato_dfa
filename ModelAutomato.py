#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Gustavo Nogueira

        Este programa aceita como entrada a Definição	do	alfabeto,
        Definição	dos	estados, Definição	do	estado	inicial,
        Definição	dos	estados	finais, Definição	da	função	de	transição e a
        Lista	de	palavras.
        O programa informa as quais palavras foram aceitas e quais foram rejeitadas.
        Informa também o processamento – informando qual o estado	correntea cada símbolo lido.

"""

from ControllerAutomato import automatos
from ViewAutomato import Saidas

if __name__ == "__main__":
    # definindo objeto do automatos
    nfa = automatos()
    saidas = Saidas()


    # capturando o conjunto de estados
    conjunto_estados = raw_input('Digite os estados:').split(',')


    # capturando o alfabeto
    alfabeto  = raw_input('Digite o alfabeto: ').split(',')


    # captura da função de transição e processamento
    captura_de_funcao = saidas.capturar_funcao_transicao()


    # estado inicial
    estado_inicial = raw_input('Digite o estado inicial: ')


    # estado final
    estado_final =raw_input('Digite o estado final: ')



    # lista de palavras
    lista_palavras = raw_input('Digite uma lista de palavras a serem processadas: ').split(',')


    # inicializando o automato
    nfa.iniciar_automato(conjunto_estados,alfabeto,captura_de_funcao,estado_inicial,estado_final, lista_palavras)

    # Saidas de dados para o usuário
    saidas.palavras_aceitas_recusadas(nfa.get_analise())
    saidas.processamento(nfa.get_processamento())





