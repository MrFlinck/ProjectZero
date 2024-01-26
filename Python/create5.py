caminho = 'text/test.txt'

with open(caminho, 'r') as arquivo:
    conteudo = arquivo.read()

novo_cont = conteudo.replace('joooj' , 'nova_palavra')
with open(caminho, 'w') as arquivo:
    arquivo.write(novo_cont)