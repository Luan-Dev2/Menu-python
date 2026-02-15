def menu():
    print('Menu'^20)
    print()
    print('1- Somar')
    print('2- Subtrair')
    print('3- Dividir')
    print('4- Multiplicar')
    print('5- Desconto do produto')
    print('6- Aumento do salário de um funcionário')
    print('0- Sair do programa')

def somar():
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    soma = num1 + num2
    return f'O resultado da soma entre os números {num1} e {num2} é {soma}.'

def subtrair():
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    sub = num1 - num2
    return f'O resultado da subtração é {sub}'

def dividir():
    print('Ainda vou fazer!')

def multiplicar():
    print('Ainda vou fazer!')

def descontoProduto():
    print('Ainda vou fazer!')

def aumentoSalarial():
    print('Ainda vou fazer!')

while True:
    menu()
    op = int(input('Escolha: '))
    if op == 1:
        print(somar())
    elif op == 2:
        print(subtrair())
    elif op == 3:
        dividir()
    elif op == 4:
        multiplicar()
    elif op == 5:
        descontoProduto()
    elif op == 6:
        aumentoSalarial()
    elif op == 0:
        print('ERRO! Tente novamente!')
        continue