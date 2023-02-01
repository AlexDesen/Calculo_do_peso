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
        if opcao == 'homem':
            altura = input('Digite sus alatura: ')
            a = float(altura)
            resultado = peso_homem(a)
            print (f'O peso é de um {opcao} e ele esta pesando {resultado:.2f} quilos.')
    print('VOCÊ FINALIZOU O PROGRAMA')    