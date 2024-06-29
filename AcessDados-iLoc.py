import pandas as pd
import numpy as np

# Vamos ler uma base de dados CSV
dataset = pd.read_csv('dase_dados/census.csv')
print(dataset)
print(type(dataset))

# Estamos trazendo apenas a coluna idade
serie_idade = dataset['age']
print(serie_idade)

# Retornando como array numpy
print(dataset['age'].values, type(dataset['age'].values))

# Retorna os 5 primeiros elementos
print(serie_idade.head())

# Retorna os 10 primeiros elementos
print(serie_idade.head(10))

# Retorna os ultimos registros
print(serie_idade.tail())

# Retorna os ultimos 10 registros
print(serie_idade.tail(10))