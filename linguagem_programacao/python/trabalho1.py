import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('linguagem_programacao/python/historico-alg1_SIGA_ANONIMIZADO.csv', sep=',')

df = df[df['tipo'] != 'EQUIVALENCIA']
df['status'] = df['status'].str.replace('Reprovado','R-freq')

df['rep_nota'] = df['status'] == 'R-nota'
df['rep_nota_int'] = 0
df.loc[df['rep_nota'], 'rep_nota_int'] = 1

df['rep_freq'] = df['status'] == 'R-freq'
df['rep_freq_int'] = 0
df.loc[df['rep_freq'], 'rep_freq_int'] = 1

df['rep_todos'] = ((df['status'] == 'R-freq') | (df['status'] == 'R-nota'))
df['rep_todos_int'] = 0
df.loc[df['rep_todos'], 'rep_todos_int'] = 1

df['status_cancelado'] = df['status'] == 'Cancelado'
df['status_cancelado_int'] = 0
df.loc[df['status_cancelado'], 'status_cancelado_int'] = 1

df['sit_evasao'] = df['situacaoDiscente'] == 'Evasão'
df['sit_evasao_int'] = 0
df.loc[df['sit_evasao'], 'sit_evasao_int'] = 1

df['periodo_grupo'] = 'anos_referencia'
df.loc[df['ano'] >= 2020 , 'periodo_grupo'] = 'anos_pandemia'
df.loc[(df['ano'] == 2022) & (df['periodo'] == '1') , 'periodo_grupo'] = 'semestre_hib_22_1'
df.loc[(df['ano'] == 2022) & (df['periodo'] == '2') , 'periodo_grupo'] = 'semestre_hib_22_2'

aprovados = df[df['status']=='Aprovado']
rep_nota = df[df['status']=='R-nota']
rep_freq = df[df['status']=='R-freq']

# 1. Qual é a média de nota dos aprovados (no período total e por ano)?
r11 = aprovados['nota'].mean().round(2)
print('\n1. Média de nota dos aprovados no período total:')
print(r11)
r12 = aprovados.groupby('ano')['nota'].mean().round(2)
print('\n1. Média de nota dos aprovados por ano: ')
print(r12)

# 2. Qual é a média de nota dos reprovados por nota (período total e ano)?
r21 = rep_nota['nota'].mean()
print('\n2. Média de nota dos reprovados por nota no período total:')
print(r21)
r22 = rep_nota.groupby('ano')['nota'].mean()
print('\n2. Média de nota dos reprovados por nota por ano: ')
print(r22)

# 3. Qual é a frequência dos reprovados por nota (período total e por ano)?
r31 = df['rep_nota_int'].mean()
print('\n3. Frequência dos reprovados por nota no período total:')
print(r31)
r32 = df.groupby('ano')['rep_nota_int'].mean()
print('\n3. Frequência dos reprovados por nota por ano: ')
print(r32)

# 4. Qual a porcentagem de evasões (total e anual)?
r41 = df['sit_evasao_int'].mean()
print('\n4. Porcentagem de evasões no período total:')
print(r41)
r42 = df.groupby('ano')['sit_evasao_int'].mean()
print('\n4. Porcentagem de evasões por ano: ')
print(r42)

# 5. Como os anos de pandemia impactaram no rendimento dos estudantes em relação aos anos anteriores,
# considerando o rendimento dos aprovados, a taxa de cancelamento e as reprovações?
# Considere como anos de pandemia os anos de 2020 e 2021.
gp_ref = 'anos_pandemia'
gp_comp = 'anos_referencia'

print(f'\n5. Comparando os {gp_ref} com os {gp_comp} (anos anteriores):')

rendimento_aprovados = aprovados.groupby('periodo_grupo')['nota'].mean()
rendimento_aprovados = rendimento_aprovados[[gp_ref,gp_comp]]
print('\nMédia de nota dos aprovados:')
print(rendimento_aprovados)

comp_rendimento = (rendimento_aprovados[gp_ref] / rendimento_aprovados[gp_comp])
print(f'\nComparação de média de nota dos aprovados ({gp_ref} / {gp_comp}):')
print(comp_rendimento)


taxa_cancelamento = df.groupby('periodo_grupo')['status_cancelado_int'].mean()
taxa_cancelamento = taxa_cancelamento[[gp_ref,gp_comp]]
print('\nTaxa de cancelamento dos períodos:')
print(taxa_cancelamento)

comp_taxa_cancelamento = (taxa_cancelamento[gp_ref] / taxa_cancelamento[gp_comp])
print(f'\nComparação da taxa de cancelamento ({gp_ref} / {gp_comp}):')
print(comp_taxa_cancelamento)


taxa_reprovacao = df.groupby('periodo_grupo')['rep_todos_int'].mean()
taxa_reprovacao = taxa_reprovacao[[gp_ref,gp_comp]]
print('\nTaxa de reprovação dos períodos:')
print(taxa_reprovacao)

comp_taxa_reprovacao = (taxa_reprovacao[gp_ref] / taxa_reprovacao[gp_comp])
print(f'\nComparação da taxa de reprovação ({gp_ref} / {gp_comp}):')
print(comp_taxa_reprovacao)

# 6. Compare a volta às aulas híbrida (2022 período 1) com os anos de pandemia e os anos anteriores.
gp_ref = 'semestre_hib_22_1'
gp_comp = 'anos_pandemia'

print(f'\n6. Comparando os {gp_ref} com os {gp_comp}:')

rendimento_aprovados = aprovados.groupby('periodo_grupo')['nota'].mean()
rendimento_aprovados = rendimento_aprovados[[gp_ref,gp_comp]]
print('\nMédia de nota dos aprovados:')
print(rendimento_aprovados)

comp_rendimento = (rendimento_aprovados[gp_ref] / rendimento_aprovados[gp_comp])
print(f'\nComparação de média de nota dos aprovados ({gp_ref} / {gp_comp}):')
print(comp_rendimento)


taxa_cancelamento = df.groupby('periodo_grupo')['status_cancelado_int'].mean()
taxa_cancelamento = taxa_cancelamento[[gp_ref,gp_comp]]
print('\nTaxa de cancelamento dos períodos:')
print(taxa_cancelamento)

comp_taxa_cancelamento = (taxa_cancelamento[gp_ref] / taxa_cancelamento[gp_comp])
print(f'\nComparação da taxa de cancelamento ({gp_ref} / {gp_comp}):')
print(comp_taxa_cancelamento)


taxa_reprovacao = df.groupby('periodo_grupo')['rep_todos_int'].mean()
taxa_reprovacao = taxa_reprovacao[[gp_ref,gp_comp]]
print('\nTaxa de reprovação dos períodos:')
print(taxa_reprovacao)

comp_taxa_reprovacao = (taxa_reprovacao[gp_ref] / taxa_reprovacao[gp_comp])
print(f'\nComparação da taxa de reprovação ({gp_ref} / {gp_comp}):')
print(comp_taxa_reprovacao)

# 7. Compare a volta às aulas presencial (2022 período 2) com a volta híbrida do item anterior.
n_alunos = df[df['ano'] == 2022].drop_duplicates(subset=['matricula','ano','periodo'])
n_aluno = n_alunos.groupby('periodo_grupo')['matricula'].count()
print(f'\n7. Comparando o número de alunos matriculados em cada semestre de 2022:')
print(n_aluno)
print(f'\nComparação do número de alunos matriculados (semestre_hib_22_2 / semestre_hib_22_2):')
print(n_aluno['semestre_hib_22_2'] / n_aluno['semestre_hib_22_1'])
print('\n*Como os dados do segundo semestre de 2022 constam com o semestre em andamento,\nnão há como comparar as notas e taxas de cancelamento e reprovação como anteriormente.')

gr12 = r12.plot(kind='bar')
gr12.bar_label(gr12.containers[0],size=10)
plt.show()

gr12 = r12.plot(kind='line')
points = gr12.get_lines()[0].get_xydata()
for point in points:
    gr12.text(point[0], point[1], f'{point[1]:.2f}', fontsize=10, ha='center', va='bottom')
plt.show()