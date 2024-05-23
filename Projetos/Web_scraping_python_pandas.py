
import pandas as pd
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

url = 'https://br.investing.com/equities/brazil'

request = requests.get(url, headers=header)

df = pd.read_html(request.text)
df
#-------------------------------------------------------------------


for i , tabela in enumerate(df):
  print('-----------------------------')
  print(i)
  print(tabela)


  #---------------------------------------------------------------



df = pd.DataFrame(df[0])


# ---------------------------------------------------------------


df['Último'] = df['Último']  /100
df['Máxima'] = df['Máxima']  /100
df['Mínima'] = df['Mínima'] /100