import pandas as pd

#Analise exploratoria de dados - Medidas de tend. central - MEDIA:
ast = pd.read_csv('../../astronauts.csv')
dados_continuos = ast['Space Flight (hr)'].dropna().astype(float)
print("MEDIA:", dados_continuos.mean())

print()

#Analise exploratoria de dados - Medidas de tend. central - MEDIANA:
print("MEDIANA", dados_continuos.median())

print()

#Analise exploratoria de dados - Medidas de tend. central - MODA:
print("MODA:", dados_continuos.mode())