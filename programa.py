valor_total = 0
compras = []
cont = 0
import os
def menu():
    print(
    '''
    01-Picanha-30.99
    02-Frango-19.90
    03-Macarrão-5.00
    42-Biscoito-5.30
    ''')

menu()

cod_produto = str(input('Digite o código do produto desejado: '))


def achar_item(cod_produto):
    global valor_total, qnt, cont
    arq = open('Produtos.txt', 'r')
    for i in arq:
        i = i.replace(f'\n', '')
        cod, nome, preco = i.split('-', 3)
        if cod == cod_produto:
            preco = float(preco)
            qnt = int(input('Digite a quantidade desejada: '))
            compras.append(qnt)
            compras.append(nome)
            valor = preco * qnt
            valor_total += valor
            compras.append(valor)
    arq.close()
    terminar = str(input('Deseja terminar? s/n '))
    if terminar == 'n':
        os.system('cls')
        menu()
        cod_produto = str(input('Digite o código do produto desejado: '))
        achar_item(cod_produto)
    else:
        os.system('cls')
        nota = open('notaFiscal.txt', 'a')
        for i in range(len(compras)//3):
            for j in range(3):
                nota.write(f'{compras[cont]}')
                if j != 2:
                    nota.write(" - ")
                cont += 1
            nota.write(f'\n')
        valor_total = str(valor_total)
        nota.write(f'Total: {valor_total}')
        nota.close()

        print("===//===//===Nota Fiscal===//===//===\n")
        for i in range(len(compras)//3):
            for j in range(1):
                print(f"O código do produto é: {compras[j]}    Nome do produto: {compras[j+1]}   Total do produto = R${compras[i+2]:.2f}")
        valor_total = float(valor_total)
        print(f"Total: R${valor_total:.2f}")


achar_item(cod_produto)
