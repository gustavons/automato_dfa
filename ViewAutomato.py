#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Saidas:
    """ saida do processamento das palavras"""
    def processamento(self, dic_processamento):
        print '\n\nProcessamento:'
        for palavra in dic_processamento.keys():
            print palavra
            a =''
            for process in dic_processamento[palavra]:
                 a += '  =>  ' + process

            print a
        return dic_processamento
    """Retorno da analise das palavras """
    def palavras_aceitas_recusadas(self, dic_palavras):
        print '\n\nAnálise:'

        for palavra in dic_palavras.keys():
            a = ''
            if dic_palavras[palavra]:
                a +=  palavra + ' = ' + 'Aceita'
            else:
                a += palavra + ' = ' + 'Rejeitada'
            print a
        return dic_palavras
    """Entrada da função de transição"""
    def capturar_funcao_transicao(self):

        condicao = True;

        funcao_transicao = []

        while True:
            a = raw_input('Digite funcao de transicao ou // para finalizar:')
            if a == '//':
                condicao = False
                break;

            fazer_teste = a.split('=')
            for fun in funcao_transicao:
                if (fun.split('=')[0] == fazer_teste[0]):
                    print 'Este programa só aceita automatos deterministicos, portanto [' + a + "] será ignorada!"
            funcao_transicao.append(a)

        return funcao_transicao

