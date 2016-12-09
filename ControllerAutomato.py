#!/usr/bin/env python
# -*- coding: utf-8 -*-


class automatos:

    def iniciar_automato(self, conjunto_estados, alfabeto, funcao_transicao, estado_inicial, estado_final, palavras):
        """Iniciando o automato DFA"""
        self.estados = conjunto_estados
        self.alfabeto = alfabeto
        self.funcao_de_transicao = funcao_transicao
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.palavras = palavras
        self.processando_estados = {}

        self.realiza_operacoes()


    """Chama todos os metodos para realizar as operações"""
    def realiza_operacoes(self):
        self.tratar_transicao(self.funcao_de_transicao, self.estados, self.alfabeto)
        self.validar_palavra(self.palavras)
        self.processamento_palavra(self.palavras)



    """Realiza o processamento das palavras, gera um com as palavras aceitas"""
    def validar_palavra(self, palavras):
        
        # dicionario para armazenar lista de palavras aceitas(True) e rejeitadas(False)
        palavras_processadas={}

        # verificar todas palavras
        for palavra in palavras:
            estado_atual = self.estado_inicial
            """ Sentinela para auxiliar na verificação das palavras, se ela pertencem ou não ao alfabeto,
                ou se ela não é aceitável"""
            passou = True 

            # Salvar processamento
            self.processando_estados.update(dict([(palavra, [])]))

            # Capturar cracteres da palavra
            for transicao in palavra:

                # verificar se pertence ou não ao alfabeto
                if (transicao in self.alfabeto):

                    # checar proximo estado
                    proximo_estado = self.verificar_transicao(estado_atual,transicao)

                    if(proximo_estado != False):
                        # Se o estado for valido ser salco o processo do estado atual
                        self.processando_estados[palavra].append(estado_atual+transicao)
                        estado_atual = proximo_estado
                    else:
                        # caso a transição não possuir estado valido
                        passou = False;
                        break
                else:
                    # caso o caracter não pertença ao alfabeto, o processamento é interropido
                    passou=False
                    break

            if(estado_atual == self.estado_final and passou):
                # add ultimo estado ao procesamento
                self.processando_estados[palavra].append(estado_atual)
                # Se a palavra for aceita será salvo um dicionario com a palavra e o valor booleano True
                palavras_processadas.update(dict([(palavra, True)]))

            else:
                # Se a palavra for rejeitada será salvo um dicionario com a palavra e o valor booleano False
                palavras_processadas.update(dict([(palavra, False)]))


        self.analise =  palavras_processadas

    """"Transformar a transição de uma string para um dicionario """
    def tratar_transicao(self, funcao_transicao, estados, alfabeto):
        # dicionario
        funcao_transicao_comple = {}

        cont = 0
        # operar todas as funções digitadas
        for transicao in funcao_transicao:
            # criar uma lista com a função de transição
            temp = transicao.split(',')

            # verificar se o estado esta definido
            if temp[cont] in estados:
                estado = temp[cont]
                # verificar se a chave existe
                if (funcao_transicao_comple.has_key(estado) != True):
                    funcao_transicao_comple.update(dict([(estado,{})]))
            else:
                # caso algo de errado o programa para e sai
                print 'Erro na transicao', transicao, 'estado', temp[cont],' nao definido\n' \
                                                                           'Defina o estado e tenter novamente'
                return exit()
            temp = temp[cont+1].split('=')
            if temp[cont] in alfabeto :#verificar se a transição exite no alfabeto

                # Ignorar estados repetidos
                if (temp[cont] not in funcao_transicao_comple[estado].keys()):
                    if temp[cont+1] in estados:# verificar se o estado de destino esta definido

                        funcao_transicao_comple[estado] = self.multiplos_caminhos(funcao_transicao_comple[estado],temp[cont],
                                                                                  temp[cont+1])

                    else:
                        # caso algo de errado o programa para e sai

                        print 'Erro na transicao', transicao, 'estado', temp[cont], ' nao definido\n' \
                                                                                    'Defina o estado e tenter novamente'
                        return exit()
            else:
                # caso algo de errado o programa para e sai

                print 'Erro na transicao', transicao, 'transicao', temp[cont], ' nao definida\n' \
                                                                            'Defina o estado e tenter novamente'
                return exit()
        self.funcao_de_transicao = funcao_transicao_comple

    """realiza o processamento da para cada estado alcançado"""
    def processamento_palavra(self, palavras):
        # dicionario
        processamento = {}

        # verificar todas as palavras
        for palavra in palavras:
            processamento.update(dict([(palavra, [])]))

            # variavel pra os estados do processamento
            a = ''

            # lista auxiliar para armazenar a palavra em forma de lista
            lista_aux = self.transformar_palavra_em_lista(palavra)
            # contador para auxiliar no processamento

            # percorrer toda a palavra
            for j in range(0, len(self.processando_estados[palavra])):
                # self.processando_estados[estado]:
                caracteres = ''

                # concatenar caracteres antes do estado que estar sendo processado
                for k in range(0, j):
                    caracteres = caracteres + lista_aux[k]
                # juntar as partes
                a = caracteres + self.processando_estados[palavra][j]

                caracteres = ''
                # concatenar caracteres depois do estado que estar sendo processado
                for l in range(j + 1, len(lista_aux)):
                    caracteres = caracteres + lista_aux[l]

                a += caracteres

                # salvar processamento
                processamento[palavra].append(a)
                a = ''

        self.processamento = processamento


    """Verifica se a transição é valida"""
    def verificar_transicao(self, estado_atual, transicao):
        try:
            proximo_estado = self.funcao_de_transicao[estado_atual][transicao]
            return proximo_estado
        except KeyError:
            return False


    """Retorna um dicionario com as palavras anaalizadas"""
    def get_analise(self):
        return self.analise


    """Retornar processamento"""
    def get_processamento(self):
        return self.processamento

    """Retorna função de transição final"""
    def get_funcao_transicao(self):
        return self.funcao_de_transicao

    def transformar_palavra_em_lista(self, palavra):
        lista_palavra = []
        for letra in palavra:
            lista_palavra.append(letra)

        return lista_palavra

    """função para que um estado possa ter uma transição para mais de um estado"""
    def multiplos_caminhos(self, dic, chave, valor):
        chace_dic = []
        valor_dic = []

        # criado lista de chaves
        chace_dic = dic.keys()
        valor_dic = dic.values()

         # adiconado chave nova
        chace_dic.append(chave)
        # adicionando novo valor
        valor_dic.append(valor)

        dic = dict.fromkeys(chace_dic,'')
        num_valor = 0
        for chav in chace_dic:

            dic[chav] = valor_dic[num_valor]
            num_valor+=1

        return dic