# Calculadora 
'''
Versão: 1.0
Resp: Yasmin Fermino
Data: 20230508

'''

print(f'''Olá, bem vindo a Calculadora. 
	Digite o número da operação que deseja realizar:
	1. Adição
	2. Subtração
	3. Divisão
	4. Multiplicação
 
 ''')

oper=input('Item:')

if 0 < int(oper) <=4:
    num1=int(input('Insira o primeiro número: '))
    num2=int(input('Insira o segundo número:'))
    if oper == '1':
        resultado = num1+num2 
        print(f'O resultado da sua Adição: {resultado}')
    elif oper == '2':
        resultado = num1-num2 
        print(f'O resultado da sua Subtração: {resultado}')
    elif oper == '3':
        resultado = num1/num2 
        print(f'O resultado da sua Divisão: {resultado}')
    else:
        resultado = num1*num2 
        print(f'O resultado da sua Multiplicação: {resultado}')
else: 
    print('Desculpa digite uma opção disponivel')