
nome = 'yuuya' 
altura = 1.60 
peso = 60 
imc = peso / altura ** 2
'f-strings'
linha_1 = f'{nome} tem {altura:.1f} de altura'
linha_2 = f'{nome} tem {altura:.2f} de altura' #o 2f add 2 casas decimais 
print(linha_1)
print(linha_2)
a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={}'.format(a,b,c) # o format pega os dados dos variaiveis e printa 
print(formato)
string = 'a={1} b={0} c={0}'
formato2 = string.format(a, b, c)
print(formato2)
string2 = 'a={} b={nome2} c={nome2}'
formato3 = string2.format(
    a, nome2=b, nome3=c
)
print(formato3)
nome = input('digite o seu nome')
print(f'o seu nome é {nome}')