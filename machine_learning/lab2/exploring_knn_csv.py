import pandas as pd

df = pd.read_csv('resultados_class_knn.csv')

df_euc = df[df['Metric'] == 'euclidean']
df_man = df[df['Metric'] == 'manhattan']
df_min = df[df['Metric'] == 'minkowski']

print('\n==================== ACCURACY ====================\n')

df1 = df.groupby(['Metric']).max(['Accuracy'])[['Accuracy']]
print(df1)

print('\n========== euclidean ==========\n')

df1 = df_euc.groupby(['Neighbors']).max(['Accuracy'])[['Accuracy']]
print(df1)

df1 = df_euc.groupby(['BatchSize']).max(['Accuracy'])[['Accuracy']]
print(df1)

print('\n========== manhattan ==========\n')

df1 = df_man.groupby(['Neighbors']).max(['Accuracy'])[['Accuracy']]
print(df1)

df1 = df_man.groupby(['BatchSize']).max(['Accuracy'])[['Accuracy']]
print(df1)

print('\n========== minkowski ==========\n')

df1 = df_min.groupby(['Neighbors']).max(['Accuracy'])[['Accuracy']]
print(df1)

df1 = df_min.groupby(['BatchSize']).max(['Accuracy'])[['Accuracy']]
print(df1)

print('\n==================== TIME ====================\n')

df1 = df.groupby(['Metric']).mean(['TotalTime'])[['TotalTime']]
print(df1)

print('\n========== euclidean ==========\n')

df1 = df_euc.groupby(['Neighbors']).mean(['TotalTime'])[['TotalTime']]
print(df1)

df1 = df_euc.groupby(['BatchSize']).mean(['TotalTime'])[['TotalTime']]
print(df1)

print('\n========== manhattan ==========\n')

df1 = df_man.groupby(['Neighbors']).mean(['TotalTime'])[['TotalTime']]
print(df1)

df1 = df_man.groupby(['BatchSize']).mean(['TotalTime'])[['TotalTime']]
print(df1)

print('\n========== minkowski ==========\n')

df1 = df_min.groupby(['Neighbors']).mean(['TotalTime'])[['TotalTime']]
print(df1)

df1 = df_min.groupby(['BatchSize']).mean(['TotalTime'])[['TotalTime']]
print(df1)
