print("programa ano em idade em uma planilia")
import pandas as pd
import datetime

import numpy as np


#criando nomes e nascimento para adicionar a planilia
nome = ['rafa', 'kaua', 'tiago']
mes_nascimento = [11, 6, 9]
nascimento = [2005, 1999, 2007]


#pegando data atual
relogio_atual = datetime.datetime.now()
ano_atual = relogio_atual.year 
data_atual = relogio_atual.month

#criando coluna
list = {'nome': nome, 'nascimento': nascimento, 'mes_nascimento' : mes_nascimento}

df1 = pd.DataFrame(list)
data = [data_atual]* len(df1['mes_nascimento'])
print(data)
df1['idade'] = (ano_atual - df1['nascimento']) - (df1['mes_nascimento'] > data)


    
print(df1)
