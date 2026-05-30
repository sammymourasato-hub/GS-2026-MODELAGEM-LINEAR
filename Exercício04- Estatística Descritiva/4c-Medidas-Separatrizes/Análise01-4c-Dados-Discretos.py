import pandas as pd

#Medidas Separatrizes - QUARTIL:
ast = pd.read_csv('../../astronauts.csv')
dados_discreto = ast['Space Flights'].dropna().astype(int)
print("Minímo:", dados_discreto.min())

print("QUARTIL:")
print(dados_discreto.quantile([0.25, 0.50, 0.75, 1.00]))

print()

