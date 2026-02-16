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
    print('Ainda vou fazer!')

def aumentoSalarial():
    print('Ainda vou fazer!')

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
        descontoProduto()
    elif op == 6:
        aumentoSalarial()
    elif op == 0:
        print(f'Saindo...')
        sleep(3)
        break
    else:
        print('ERRO! Tente novamente!')
        continue
    print('='*50)
    sleep(2)