nome = input('digite o seu nome: ')
print(f'o seu nome é {nome}')

numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')
numero_3 = int(numero_2) + int(numero_1)
print(f'A soma de dois números é: {numero_3}')

entrada = input('Você quer "entrar" ou "sair"? ')
if entrada == 'entrar':
    print('Você entrou no sistema')

elif entrada == 'sair':
    print('Você saiu do sistema')

else:
    print('Você não digitou nem entrar nem sair..')

