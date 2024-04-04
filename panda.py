import pandas as pd
import datetime

import numpy as np


#criando nomes e nascimento para adicionar a planilia
nome = ['rafa', 'kaua', 'tiago']
nacimento = [2005, 1999, 2007]

#criando coluna
list = {'nome': nome, 'nascimento': nacimento}

#pegando data atual
data_atual = datetime.datetime.now()
data_atual = data_atual.year 

df1 = pd.DataFrame(list)
df1['idade'] = data_atual - df1['nascimento']

print(df1)
