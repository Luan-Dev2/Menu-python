from time import sleep

def menu():
    print(f'{"Menu":^20}')
    print()
    print('1- Somar.')
    print('2- Subtrair.')
    print('3- Dividir.')
    print('4- Multiplicar.')
    print('5- Desconto do produto.')
    print('6- Aumento do salário de um funcionário.')
    print('0- Sair do programa.')

def somar():
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))
    soma = num1 + num2
    return f'O resultado da soma entre os números {num1} e {num2} é {soma:.2f}.'

def subtrair():
    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))
    sub = num1 - num2
    return f'O resultado da subtração é {sub:.2f}.'

def dividir():
    num1 = float(input('Número que vai ser dividido: '))
    num2 = float(input('Número eu vai dividir: '))
    result = num1 / num2
    return f'O resultado da divisão de {num1} por {num2} é {result:.2f}.'


def multiplicar():
    num1 = float(input('Digite o número que vai ser multiplicado: '))
    num2 = float(input('Digite o número que vai multiplicar: '))
    result = num1 * num2
    return f'O resultado da multiplicação é {result:.2f}.'

def descontoProduto():
    valorProduto = float(input('Digite o valor do produto: R$'))
    valorDesconto = int(input('Digite a porcentagem do desconto: '))
    produtoDesconto = valorProduto - (valorProduto * valorDesconto/100)
    return f'O produto que era R${valorProduto} passa a ser R${produtoDesconto:.2f} com o desconto de {valorDesconto}%.'

def aumentoSalarial():
    valorSalario = float(input('Valor do salário do(a) funcionário(a): R$'))
    valorAumento = int(input('Valor da porcentagem do aumento: '))
    salarioNovo = valorSalario + (valorSalario * valorAumento/100)
    return f'O salário do(a) funcionário(a) passa a ser R${salarioNovo:.2f} com {valorAumento:.2f} de aumento.'

while True:
    menu()
    op = int(input('Escolha: '))
    print('='*50)
    if op == 1:
        print(somar())
    elif op == 2:
        print(subtrair())
    elif op == 3:
        print(dividir())
    elif op == 4:
        print(multiplicar())
    elif op == 5:
        print(descontoProduto())
    elif op == 6:
        print(aumentoSalarial())
    elif op == 0:
        print(f'Saindo...')
        sleep(3)
        break
    else:
        print('ERRO! Tente novamente!')
        continue
    print('='*50)
    sleep(2)