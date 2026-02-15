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
    print('Ainda vou fazer!')

def subtrair():
    print('Ainda vou fazer!')

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
        somar()
    elif op == 2:
        subtrair()
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