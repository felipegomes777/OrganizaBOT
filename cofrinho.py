import json
from datetime import datetime

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
    print('')
    print('-=-'*5,'OrganizaBOT','-=-'*5)
    print('\n1) Adicionar receita.')
    print('2) Adicionar gastos.')
    print('3) Ver Saldo.')
    print('4) Histórico.')
    print('5) Relatório.')
    print('6) Sair.')

    opcoes = input('Escolha: ').upper()
    hist = 0
    total_receitas = 0
    total_gastos = 0
    saldoG = 0
    maiorG = 0
    contador = 0
    if opcoes == 'ADICIONAR RECEITA' or opcoes == '1':
        try:
            valor = float(input('Quanto deseja adicionar de receita? '))
        except ValueError:
            print('Digite apenas numeros!')
            continue
        descricao = input('descricao: ')
        categoria = input('Categoria: ')
        data = datetime.today().strftime('%d/%m/%Y %H:%M')
        saldo += valor

        historico.append({
            "Data": data,
            "tipo": "receita",
            "valor": valor,
            "descricao": descricao,
            "categoria": categoria
        })
        with open('dados.json', 'w') as arquivo:
            json.dump(historico, arquivo)

    elif opcoes == 'ADICIONAR GASTOS' or opcoes == '2':
        try:
            valor = float(input('Quanto foi seus gastos? '))
        except ValueError:
            print('Digite apenas números!')
            continue
        descricao = input('descricao: ')
        categoria = input('Categoria: ')

        data = datetime.today().strftime('%d/%m/%Y %H:%M')

        saldo -= valor

        historico.append({
            "Data": data,
            "tipo": "gasto",
            "valor": valor,
            "descricao": descricao,
            "categoria": categoria
        })

        with open('dados.json', 'w') as arquivo:
            json.dump(historico, arquivo)

    elif opcoes == 'VER SALDO' or opcoes == '3':
        print('Seu saldo é de {:.2f}'.format(saldo))

    elif opcoes == 'HISTORICO' or opcoes == '4':
        print('1) Apenas receitas')
        print('2) Apenas gastos')
        print('3) Total')
        hist = str(input('Escolha: '))
        if hist == '1':
            print('Historico:')
            for i in historico:
                if i['tipo'] == 'receita':
                    print(f"{i['Data']} | {i['tipo']} | {i['valor']:.2f} | {i['categoria']}")
        elif hist == '2':
            print('Historico:')
            for i in historico:
                if i['tipo'] == 'gasto':
                    print(f"{i['Data']} | {i['tipo']} | {i['valor']:.2f} | {i['categoria']}")
        elif hist == '3':
            print('Histórico:')
            for i in historico:
                print(f"{i['Data']} | {i['tipo']} | R${i['valor']:.2f} | {i['descricao']:} | {i['categoria']}")
        else:
            print('Opção inválida!')
    elif opcoes == 'RELATÓRIOS' or opcoes == '5':
        print('1) Total de receitas')
        print('2) Total de gastos')
        print('3) Saldo Geral')
        print('4) Maior gasto')
        print('5) Quantidade de transições')
        esc = input('Escolha: ')

        valor = total_receitas
        if esc == '1':
            for i in historico:
                if i['tipo'] == 'receita':
                    total_receitas += i['valor']
            print("Receitas: R${}".format(total_receitas))
        elif esc == '2':
            for i in historico:
                if i['tipo'] == 'gasto':
                    total_gastos += i['valor']
            print("Gastos: R${}".format(total_gastos))
        elif esc == '3':
            for i in historico:
                if i['tipo'] == 'receita':
                    total_receitas += i['valor']
                if i['tipo'] == 'gasto':
                    total_gastos += i['valor']
            saldoG = total_receitas - total_gastos
            print('o Saldo geral é de: R${}'.format(saldoG))
        elif esc == '4':
            for i in historico:
                if i['tipo'] == 'gasto':
                    if i['valor'] > maiorG:
                        maiorG = i['valor']
            print('O maior gasto foi de R${}'.format(maiorG))
        elif esc == '5':
            for i in historico:
                contador += 1
            print('Existem {} transações'.format(contador))
    elif opcoes == 'SAIR' or opcoes == '6':
        print('Saindo...')
        break

    else:
        print('Operação inválida!')
