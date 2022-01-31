# -*- coding: iso-8859-1 -*-

print('Exercícios Python:')
print('-----------------------------')

print('\n 1 - Exibir o número digitado pelo usuário')
print('\n 2 - Exibir lista de frutas')
print('\n 3 - Exibir a soma de 2 números digitados pelo usuário')
print('\n 4 - Programa que converta metros em centímetros')
print('\n 5 - Um programa que calcule a área de um círculo a partir do raio digitado')
print('\n 6 - Um programa de calcule a área de um quadrado e depois mostre o dobro desse valoro')

print('\n-----------------------------')

print('\n Selecione um exercício da lista: ')

# Switch case para exibição dos exercício:

def func1():
    a = input('\n1 - Digite um numero: ')
    print('O número digitado foi: ', a)
    print('\n-----------------------------')

def func2():
    print('\n2 - Lista de frutas:')
    frutas = ['Maça', 'Banana','Cereja']
    x, y, z = frutas
    print(x, y, z)
    print('\n-----------------------------')

def func3():
    print('\n3 - Digite 2 numeros e imprima a soma deles: ')
    n1 = input('\n Digite o primeiro numero: ')
    n2 = input('Digite o segundo numero: ')
    soma = int(n1) + int(n2)
    print('\nO resultado da soma dos numeros é:', soma)
    
    #Por default um input retorna uma string, por isso, é importante colocarmos o int.
    print('\n-----------------------------')

def func4():
    print('4 - Um programa que converta metros em centimetros:\n')
    m = int(input('Qual a distância em metros? '))
    print('Essa distância em centímetros é: {}cm '.format(m*100))
    
    print('\n-----------------------------')

def func5():
    print('5 - Um programa que calcule a área de um círculo a partir do raio digitado: ')
    r = int(input('Digite o raio do círculo: '))
    print('A área desse círculo é: ', r ** 2)
    print('\n-----------------------------')

def func6():
    print('6 - Um programa de calcule a área de um quadrado e depois mostre o dobro desse valoro: ')
    r = int(input('Digite a medida de um dos lados: '))
    print('A área desse quadrado é: ', r*r)
    print('O dobro da área desse quadrado é: ', (r*r)*2)
    print('\n-----------------------------')

def func0():
    exit()

def default():
    print("Opção inválida")

if __name__ == "__main__":
    switch = {
        "1": func1,
        "2": func2,
        "3": func3,
        "4": func4,
        "5": func5,
        "6": func6,
        "0": func0
    }

    case = switch.get(input(), default)
    case()
