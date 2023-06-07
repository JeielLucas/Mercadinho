import os

valor_total = 0
compras = []
cont = 0

def menu():
    arquivo = open("Produtos.txt", "r")
    arqProdutos = arquivo.readlines()
    for i in arqProdutos:
        i = i.replace("\n", "")
        print(f"{i}")


menu()

cod_produto = str(input('Digite o código do produto desejado: '))


def achar_item(cod_produto):
    global valor_total, qnt, cont
    arq = open('Produtos.txt', 'r')
    achouCodigo = False
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
            achouCodigo = True
    arq.close()
    if(achouCodigo == False):
        print("Código inexistente")
    terminar = str(input('Deseja terminar? s/n '))
    if terminar == 'n':
        os.system('cls')
        menu()
        cod_produto = str(input('Digite o código do produto desejado: '))
        achar_item(cod_produto)
    else:
        os.system('cls')
        nota = open('notaFiscal.txt', 'w')
        for i in range(len(compras)//3):
            for j in range(3):
                nota.write(f'{compras[cont]}')
                if j != 2:
                    nota.write(" - ")
                cont += 1
            nota.write(f'\n')
        valor_total = str(valor_total)
        nota.write(f'Total: {valor_total}')

        print("===//===//===Nota Fiscal===//===//===\n")
        for i in range(len(compras)//3):
            for j in range(1):
                print(f"O código do produto é: {compras[j]}    Nome do produto: {compras[j+1]}   Total do produto = R${compras[i+2]:.2f}")
        valor_total = float(valor_total)
        print(f"Total: R${valor_total:.2f}")
        nota.close()


achar_item(cod_produto)
