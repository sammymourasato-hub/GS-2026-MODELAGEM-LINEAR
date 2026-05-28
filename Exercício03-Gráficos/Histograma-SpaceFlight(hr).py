import matplotlib.pyplot as plt
import pandas as pd

ast = pd.read_csv('../astronauts.csv')

dados_continuos = ast['Space Flight (hr)'].dropna().astype(float).tolist()
print(dados_continuos)

intervalos = pd.cut(dados_continuos, bins=5)

plt.hist(dados_continuos, bins=5, color="green")
plt.xlabel('Horas no Espaço')
plt.ylabel('Quantidade de Astronautas')
plt.title('Distribuição de Horas no Espaço por Astronauta')
plt.show()