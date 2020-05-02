import pandas as pd
from pandas.io.json import json_normalize

df = pd.read_json(r'data/2020.json')
gastos = json_normalize(df['dados']) 
gastos['valorLiquido'] = gastos['valorLiquido'].astype(float)

gastos.info(verbose=True)

gastos_telefonia = gastos.loc[gastos['descricao'] == 'TELEFONIA']
gastos_telefonia_deputado = gastos_telefonia.groupby("nomeParlamentar")["valorLiquido"].sum().reset_index().sort_values('valorLiquido', ascending=False)

gastos_telefonia_deputado.to_json('gastos-2020.json', orient='records', lines=True)