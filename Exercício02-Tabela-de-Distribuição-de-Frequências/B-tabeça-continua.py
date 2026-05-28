#---------- TABELA CONTÍNUA DE QUANTAS HORAS OS FICARAM NO ESPAÇO ----------

from collections import Counter
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('../astronauts.csv')

dados_continuos = df['Space Flight (hr)'].dropna().astype(float).tolist()
print(dados_continuos)

intervalos = pd.cut(dados_continuos, bins=5)


fi = intervalos.value_counts().sort_index()
fia = fi.cumsum()
fr = fi / fi.sum() * 100
fra = fr.cumsum()

tabela_continua = pd.DataFrame({
    'Frequência_Absoluta': fi,
    'Frequência_Absoluta_Acumulada': fia,
    'Frequência_Relativa': fr,
    'Frequência_Relativa_Acumulada': fra,
})

tabela_continua.loc['Total'] = [fi.sum(), '-', fr.sum(), '-']

print("=== TABELA CONTÍNUA - Space Flight (hr) ===")
print(tabela_continua)