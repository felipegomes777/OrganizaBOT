import json
try:
    with open('dados.json', 'r') as arquivo:
        historico = json.load(arquivo)

except FileNotFoundError:
    historico = []
saldo = 0
for i in historico:

    if i['tipo'] == 'receita':
        saldo += i['valor']

    else:
        saldo -= i['valor']

while True:
    print('-=-'*5,'OrganizaBOT','-=-'*5)
    print('\n1) Adicionar receita.')
    print('2) Adicionar gastos.')
    print('3) Ver Saldo.')
    print('4) Histórico.')
    print('5) Sair.')

    opcoes = input('Escolha: ').upper()
    if opcoes == 'ADICIONAR RECEITA' or opcoes == '1':
        valor = float(input('Quanto deseja adicionar de receita? '))
        saldo += valor
        historico.append({
            "tipo": "receita",
            "valor": valor
        })

        with open('dados.json', 'w') as arquivo:
            json.dump(historico, arquivo)

    elif opcoes == 'ADICIONAR GASTOS' or opcoes == '2':
        valor = float(input('Quanto foi seus gastos? '))
        descricao = input('Descricação: ')
        saldo -= valor
        historico.append({
            "tipo": "gasto",
            "valor": valor
        })

        with open('dados.json', 'w') as arquivo:
            json.dump(historico, arquivo)
    elif opcoes == 'VER SALDO' or opcoes == '3':
        print('Seu saldo é de {:.2f}'.format(saldo))
    elif opcoes == 'HISTORICO' or opcoes == '4':
        print('Histórico:')
        for i in historico:
            print(f'{i['tipo']} -> R${i['valor']:.2f} -> {descricao['Descrição']:.2f}')
    elif opcoes == 'SAIR' or opcoes == '5':
        print('Saindo...')
        break
    else:
        print('Operação inválida!')
