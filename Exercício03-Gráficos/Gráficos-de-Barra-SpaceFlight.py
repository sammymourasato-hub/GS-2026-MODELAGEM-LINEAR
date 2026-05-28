from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

ast = pd.read_csv('../astronauts.csv')

dados_discreto = ast['Space Flights'].dropna().astype(int).tolist()

contagem = dict(sorted(Counter(dados_discreto).items()))
labels = list(contagem.keys())
values = list(contagem.values())

colors = ["skyblue"]

plt.bar(labels, values, color=colors)
plt.title('Distribuição de Astronautas por Número de Viagens Espaciais')
plt.xlabel('Quantidade de vezes que os astronautas foram para o espaço')
plt.ylabel('Quantidade de Astronautas')
plt.show()