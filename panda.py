print("programa idade em uma planilha")
import pandas as pd
import datetime

import numpy as np


#criando nomes e nascimento para adicionar a planilha
dado = []
nome = []
mes_nascimento = []
nascimento = []
opc =1

# Pegando mes e ano atual
relogio_atual = datetime.datetime.now()
ano_atual = relogio_atual.year 
mes_atual = relogio_atual.month
while opc != 0 :
    list = {'nome': nome, 'nascimento': nascimento, 'mes_nascimento' : mes_nascimento}
    df1 = pd.DataFrame(list)
    mes = [mes_atual]* len(nome)
    df1['idade'] = (ano_atual - df1['nascimento']) - (df1['mes_nascimento'] > mes)
    print("escolha a opção")
    print("0 - para sair do programa")
    print("1- cadastrar")
    print("2- listar")
    print("3- alterar")
    print("4- excluir")


    opc = int(input("escreva a opçao desejada: "))
    while opc < 0 or opc > 3 :
        opc = int(input("escreva a opçao desejada novamente!: "))

    match opc:
        case 1:
            dado.append(input("seu nome: "))
            while not dado[0].strip():
                dado[0] = input("seu nome novamente: ")

            dado.append(input("ano de nascimento: "))
            while len(dado[1]) < 4 or not dado[1].isdigit() or int(dado[1]) > ano_atual:
                dado[1] = input("ano de nascimento novamente: ")

            dado.append(input("mes de nascimento: "))
            while len(dado[2]) > 2 or not dado[2].isdigit() or int(dado[2]) > 12:
                dado[2] = input("mes novamente: ")

            dado[1] = int(dado[1])
            dado[2] = int(dado[2])

            nome.append(dado[0])
            nascimento.append(dado[1])
            mes_nascimento.append(dado[2])
            dado.clear()
            
        case 2:
            if len(nome) == 0:
                print("------------------")
                print("nada cadastrado")
                print("------------------")
            else:
                print(df1)
        case 3:
            if len(nome) == 0:
                print("------------------")
                print("nada cadastrado")
                print("------------------")
            
            for x in nome:
                print(x) 
            else:
                for x in range(len(nome)):
                    if input("escreva o nome da pessoa q deseja alterar") == nome[x]:
                        nome[x] = input("substitua o nome")
                        nascimento[x] = int(input("ano de nascimento: "))
                        mes_nascimento[x] = int(input("mes nascimento"))
        case 4:
            if len(nome) == 0:
                print("------------------")
                print("nada cadastrado")
                print("------------------")
            
            for x in nome:
                print(x) 
            else:
                for x in range(len(nome)):
                    if input("escreva o nome da pessoa q deseja alterar") == nome[x]:
                        del(nome[x])
                        del(nascimento[x])
                        del(mes_nascimento[x])  
                        break


        

            
            
           

