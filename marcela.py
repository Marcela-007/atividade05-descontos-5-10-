# Um comerciante quer tabelar os preços de seus produtos,
# criando um desconto de 5% para valores acima de R$50,00 e 10% para valores acima
# de R$200,00. Elabore um programa que leia o preço normal do produto e informe o
# preço com desconto

valor_produto = float(input('Insira o valor do produto: R$ '))
b = 0

def desconto1(a,b):
    if a >= 50:
        valor_5 = (a * 5) / 100
        b = a - valor_5
        print(f'O valor final do seu produto é de {b}')
    elif a >= 200:
        valor_10 = (a * 10) / 100 
        b = a - valor_10
        print(f'O valor final de seu produto é de {b}')
    else:
        print('O valor do produto fornecido não está na lista dos produtos com descontos.')

desconto1(valor_produto,b)
