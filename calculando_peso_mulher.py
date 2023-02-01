from PESO_IDEAL.fuction import peso_homem, peso_mulher

if __name__ == "__main__":
    opcao = None

    while opcao != "sair":
        
        print(30*("="))
        print('Informe se você é:')
        print('homem')
        print('ou')
        print('mulher')
        print('*Se desejar, digire sair para filnalizar o programa.')
        opcao = input('Você é homem ou mulher? ')
        if opcao == 'mulher':
            altura = input('Digite sus alatura: ')
            a = float(altura)
            resultado = peso_mulher(a)
            print (f'O peso calculado é de um {opcao} e ela esta pesando {resultado:.2f} quilos.')
    print('VOCÊ FINALIZOU O PROGRAMA')    