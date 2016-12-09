#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ControllerAutomato import automatos
from ViewAutomato import Saidas

if __name__ == "__main__":
    # definindo objeto do automatos
    nfa = automatos()
    saidas = Saidas()


    # capturando o conjunto de estados
    # conjunto_estados = raw_input('Digite os estados:').split(',')
    conjunto_estados = ['q1','q2','q3', 'q4']
    # print 'Conjuntos de estados: '
    # print conjunto_estados

    # capturando o alfabeto
    # alfabeto  = raw_input('Digite o alfabeto: ').split(',')
    alfabeto = ['a','b']
    # print 'ALfabeto: '
    # print alfabeto

    # captura da função de transição e processamento
    # captura_de_funcao = saidas.capturar_funcao_transicao()
    captura_de_funcao = ['q1,a=q2','q2,b=q3','q3,a=q2', 'q4,a=q3', 'q2,a=q4', 'q2,b=q1', 'q2,b=q4']
    # funcao_transicao = nfa.tratar_transicao(captura_de_funcao,conjunto_estados, alfabeto)
    # print 'Funcao de transicao: '
    # print funcao_transicao



    # estado inicial
    # estado_inicial = raw_input('Digite o estado inicial: ')
    estado_inicial = 'q1'
    # print 'Estado inicial: '
    # print estado_inicial

    # estado final
    # estado_final =raw_input('Digite o estado final: ')
    estado_final = 'q4'
    # print 'Estado final: '
    # print estado_final


    # lista de palavras
    # lista_palavras = raw_input('Digite uma lista de palavras a serem processadas: ').split(',')
    lista_palavras = ['aa', 'abaa', 'acc']
    # print 'Lista de palavras'
    # print lista_palavras

    # inicializando o automato
    nfa.iniciar_automato(conjunto_estados,alfabeto,captura_de_funcao,estado_inicial,estado_final, lista_palavras)

    saidas.palavras_aceitas_recusadas(nfa.get_analise())
    saidas.processamento(nfa.get_processamento())





