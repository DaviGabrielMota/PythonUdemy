"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:

    num_int = int(input('Por favor, digite um número inteiro: '))

    if num_int % 2 == 0:
        print('Par')

    else:
        print('Ímpar')

except:

    ValueError

    print(f'O número que você digitou não é inteiro. Por favor, digite novamente.')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
time_quest = int(input('Informe a hora atual da sua região: '))

if 6 < time_quest <= 12:
    print('Bom dia!')

elif 12 < time_quest <= 18:
    print('Boa tarde!')

elif 18 < time_quest <= 23:
    print('Boa noite!')

elif 00 < time_quest <= 5:
    print('Boa madrugada!')

else:
    print('Não conheço essa hora!')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
ask_first_name = input('Digite seu primeiro nome: ')

tamanho = len(ask_first_name)

if tamanho <= 4:
    print('Seu nome é curto!')

elif tamanho >= 5 and tamanho <= 6:
    print('Seu nome é normal!')  

elif tamanho > 6:
    print('Seu nome é muito grande!')