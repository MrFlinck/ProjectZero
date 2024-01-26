primeiro_valor = input('Qual é o primeiro número?')
segundo_valor = input('Qual é o segundo valor? ')
if(primeiro_valor == segundo_valor):
    print(f'o primeiro valor: {primeiro_valor} e segundo valor: {segundo_valor} são iguais')

elif(primeiro_valor > segundo_valor):
    print(f'o primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}')

else:
    print(f'o primeiro valor: {primeiro_valor} é menor que o segundo valor: {segundo_valor}')
