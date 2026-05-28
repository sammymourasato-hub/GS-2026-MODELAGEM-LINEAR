#---------- TABELA DISCRETA DE QUANTAS VEZES OS ASTRONAUTAS FORAM PARA O ESPAÇO ----------

from collections import Counter
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('../astronauts.csv')

# Variável discreta: Space Flights
dados_discreto = df['Space Flights'].dropna().astype(int).tolist()

fi = pd.Series(Counter(dados_discreto)).sort_index()
fia = fi.cumsum()
fr = fi / fi.sum() * 100
fra = fr.cumsum()

tabela_discreta = pd.DataFrame({
    'Frequência_Absoluta': fi,
    'Frequência_Absoluta_Acumulada': fia,
    'Frequência_Relativa': fr,
    'Frequência_Relativa_Acumulada': fra,
})

tabela_discreta.loc['Total'] = [fi.sum(), '-', fr.sum(), '-']

print("=== TABELA DISCRETA - Space Flights ===")
print(tabela_discreta)