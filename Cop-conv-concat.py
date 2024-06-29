import pandas as pd
import numpy as np

valores = np.random.random(10)
indexes = np.arange(0,10)
series_Dados = pd.Series(valores, indexes)
print(series_Dados)

# Maneira correta de copiar uma Serie
series_Dados2 = series_Dados.copy()
print(series_Dados2)
print(type(series_Dados2))

# Convertendo para inteiro
print(series_Dados2.astype(int))
print(series_Dados2.dtype)

series_Dados2 = series_Dados2.astype(int)
print(series_Dados2)

# Concatenação
dicionario = {'João': 10, 'Pedro': 20, 'Julia': 19, 'Leila': 39}
dict_serie_dados = pd.Series(dicionario)

dados_novos = {'Rogerio': 45, 'Rafaela': 19}
series_Dados3 = pd.Series(dados_novos)
print(series_Dados3)

print(dict_serie_dados)

series_Dados4 = pd.concat([dict_serie_dados, series_Dados3])
print(series_Dados4)