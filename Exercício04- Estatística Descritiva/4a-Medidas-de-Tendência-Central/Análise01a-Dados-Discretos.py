import pandas as pd

#Analise exploratoria de dados - Medidas de tend. central - MEDIA:
ast = pd.read_csv('../../astronauts.csv')
dados_discreto = ast['Space Flights'].dropna().astype(int)
print("MEDIA:", dados_discreto.mean())

print()

#Analise exploratoria de dados - Medidas de tend. central - MEDIANA:
print("MEDIANA", dados_discreto.median())

print()

#Analise exploratoria de dados - Medidas de tend. central - MODA:
print("MODA:", dados_discreto.mode())