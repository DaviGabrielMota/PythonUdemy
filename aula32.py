"""
Flag (Bandeira) - Marcar um local
None - Não valor
is e is not = é não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None


if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    passou_no_if = None
    print('Não faça nada')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')