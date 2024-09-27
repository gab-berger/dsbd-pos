import pandas as pd

df = pd.read_csv('resultados_classificadores.csv')

df1 = df.groupby(['BatchSize','Classifier']).max(['Accuracy'])[['Accuracy']].reset_index().sort_values(by='Accuracy',ascending=False)

print(df1[df1['BatchSize']==1000])

print(df1[df1['BatchSize']==10000])

print(df1[df1['BatchSize']==20000])

df1 = df.groupby(['BatchSize','Classifier']).mean(['TotalTime'])[['TotalTime']].reset_index().sort_values(by='TotalTime',ascending=True)

print(df1[df1['BatchSize']==1000])

print(df1[df1['BatchSize']==10000])

print(df1[df1['BatchSize']==20000])