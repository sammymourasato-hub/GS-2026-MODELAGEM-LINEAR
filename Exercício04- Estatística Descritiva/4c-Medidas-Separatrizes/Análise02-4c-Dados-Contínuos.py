import pandas as pd

#Medidas Separatrizes - QUARTIL:
ast = pd.read_csv('../../astronauts.csv')
dados_continuos = ast['Space Flight (hr)'].dropna().astype(float)
print("Minímo:", dados_continuos.min())

print("QUARTIL:")
print(dados_continuos.quantile([0.25, 0.50, 0.75, 1.00]))

print()
