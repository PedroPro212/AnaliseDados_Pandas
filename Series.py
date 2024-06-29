import pandas as pd
import numpy as np

# Example 1
series_dados = pd.Series([10, 20, 30, 40, 50])
print(series_dados)

# Example 2
array_inteiros = [10, 20, 30, 40, 50]
indices = ['A', 'B', 'C', 'D', 'E']
series_dados = pd.Series(array_inteiros, index=indices)
print(series_dados)

# Example 3 com numpy
np_array_inteiros = np.array([10, 20, 30, 40, 50])
print(np_array_inteiros)

series_dados = pd.Series(array_inteiros)
print(series_dados)

# Mostra o tamanho do array
print(series_dados.size)

# Alterar index dos dados
series_dados.index = ['Z', 'B', 'K', 'H', 'Q']
print(series_dados)

# Criando series com valores random
valores = np.random.random(10)
indexes = np.arange(0,10)
print(valores)
print(indexes)

series_dados = pd.Series(valores, indexes)
print(series_dados)

# Retornando apenas os indexes
print(series_dados.index)

# Dicionário
dicionario = {'João': 10, 'Pedro': 20, 'Julia': 19, 'Leila': 39}
print(type(dicionario))
print(dicionario)

dict_serie_dados = pd.Series(dicionario)
print(dict_serie_dados)