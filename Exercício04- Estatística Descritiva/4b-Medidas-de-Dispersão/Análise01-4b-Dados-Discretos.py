import pandas as pd

#Medidas de dispersao - MINIMO:
ast = pd.read_csv('../../astronauts.csv')
dados_discreto = ast['Space Flights'].dropna().astype(int)
print("Minímo:", dados_discreto.min())

print()

#Medidas de dispersao - MAXIMO:
print("Máximo", dados_discreto.max())

print()

#Medidas de dispersao - AMPLITUDE (DIFERENÇA ENTRE MÍNIMO E MÁXIMO:
print("Amplitude:", dados_discreto.max() - dados_discreto.min())

print()

#Medidas de dispersao - VARIANCIA:
print("Variância:", dados_discreto.var())

print()

#Medidas de dispersao - DESVIO PADRAO:
print("Desvio Padrão", dados_discreto.std())

print()

#Medidas de dispersao - Coeficiente de Variação:
print("Coeficiente de variação:", dados_discreto.std() / dados_discreto.mean() * 100)