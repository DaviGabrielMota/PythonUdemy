# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3
#  D a v i
# -6-5-4-3
# nome = 'Davi'
# print(nome[4])
# print(nome[-6])
# print('vi' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vi' not in nome)
# print('zero' not in nome)
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')