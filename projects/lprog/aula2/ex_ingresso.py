def valor_ingresso(idade):
    idade = int(idade)
    valor_base = 10
    
    if idade < 5 or idade > 70:
        ingresso = 0
    elif idade >= 18:
        ingresso = valor_base
    elif idade >= 13:
        ingresso = int(valor_base*0.8)
    else:
        ingresso = int(valor_base*0.5)
    
    print(f'O ingresso custa: R$ {ingresso},00')

def main():
    entrada = input('Qual a idade? (para sair digite "q") :')

    if entrada == 'q':
        print('Obrigado por comprar conosco!')
    else:
        valor_ingresso(entrada)
        main()        

print('Para saber o valor do ingresso, precisamos a idade de quem vai usar o ingresso!')
main()