import pandas as pd

#Medidas de dispersao - MINIMO:
ast = pd.read_csv('../../astronauts.csv')
dados_continuos = ast['Space Flight (hr)'].dropna().astype(float)
print("Minímo:", dados_continuos.min())

print()

#Medidas de dispersao - MAXIMO:
print("Máximo", dados_continuos.max())

print()

#Medidas de dispersao - AMPLITUDE (DIFERENÇA ENTRE MÍNIMO E MÁXIMO:
print("Amplitude:", dados_continuos.max() - dados_continuos.min())

print()

#Medidas de dispersao - VARIANCIA:
print("Variância:", dados_continuos.var())

print()

#Medidas de dispersao - DESVIO PADRAO:
print("Desvio Padrão", dados_continuos.std())

print()

#Medidas de dispersao - Coeficiente de Variação:
print("Coeficiente de variação:", dados_continuos.std() / dados_continuos.mean() * 100)