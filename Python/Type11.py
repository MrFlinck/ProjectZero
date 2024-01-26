nome = input('Qual é seu nome?: ')
idade = input('Quantos anos você tem?: ')
if nome and idade :
   
    print(f'Seu nome é {nome}')
    print(f'seu nome invertido é: {nome[::-1]} ' )
    if(' ' in nome):
         print('Seu nome contém espaços')
         print(f'Seu nome contém {len(nome)} letras')
         print(f'A primeira letra do seu nome é {nome[0]}')
         print(f'a ultima palavra do seu nome é {nome[len(nome) - 1]}')
   

    else:
        print('Seu nome não contem espaços')
        print(f'Seu nome contém {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'a ultima palavra do seu nome é {nome[len(nome) - 1]}')
    
    

else:
     print('Desculpe, você deixou campos vazios.')
    



