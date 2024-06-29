import pandas as pd
import numpy as np

valores = np.random.random(10)
indexes = np.arange(0,10)

series_Dados = pd.Series(valores, indexes)
print(series_Dados)

# Fatiamento (Slicing)
print(series_Dados[0:4])# Fatiamento (Slicing)
print(series_Dados[:4])

# Retornar o ultimo elemento de uma Serie
print(series_Dados[-1:])

# O ultimo indice NÃO é incluido
print(series_Dados[:-1])

# Armazanar na variavel apenas o três primeiros elementos
s2 = series_Dados[:3]
print(s2)