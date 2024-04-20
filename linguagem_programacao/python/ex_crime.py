import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('linguagem_programacao/dbs/SacramentocrimeJanuary2006.csv')

#print(df.info())
#print(df.head())
#print(df.describe())
df['datetime'] = pd.to_datetime(df['cdatetime'])
df['date'] = df['datetime'].dt.date
#df['date'] = df['cdatetime'].str.split(' ').str[0]
#df['date'] = pd.to_datetime(df['date'],dayfirst=True,infer_datetime_format=True,format="mixed")
df['month'] = df['date'].dt.month

print('1. Qual a quantidade de crimes por data?')
df_ex1 = df.groupby(['date'])['address'].count()
print(df_ex1)

print('2. Qual a porcentagem de crimes por tipo de crime no mês inteiro?')
df_ex2 = df.groupby(df['month'])['crimedescr'].value_counts(normalize=True)
print(df_ex2)

print('3. Qual a porcentagem de crimes por tipo de crime por dia?')
df_ex3 = df.groupby(df['date'])['crimedescr'].value_counts(normalize=True)
print(df_ex3)

print('4. Qual a média de ocorrências de crime (total de crimes) por distrito no mês?')
df_ex4 = df.groupby(df['month'])['district'].value_counts()
print(df_ex4)