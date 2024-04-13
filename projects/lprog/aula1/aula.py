import sys
arq_nome = sys.argv[1]
arq_handle = open(arq_nome)
texto = arq_handle.read()
linhas = texto.split("\n")
print(linhas)
print(type(linhas))
print(linhas[0])
print(type(linhas[0]))


#print('Olá mundo')
#nome = input('Digite seu nome:')
#print('Seu nome é: ', nome)
#idade = int(input('Digite sua idade:'))
#idade_apos = int(input('Com quantos anos você quer aposentar:'))
#anos_apos = idade_apos - idade
#print(nome, ', faltam ', anos_apos, 'anos para você se aposentar')