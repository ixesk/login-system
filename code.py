# Login
nome = 'root'  # Escolha um nome
senha = 9090  # Escolha uma senha (int)


cmd = input("Digite 'login' para entrar na sua conta ou 'sair' para sair: ")

if cmd == 'login':
    while cmd != 'sair':
        cmd = input('Pressione enter para prosseguir ou digite sair: ')

        n = str(input('Nome de usuario: '))
        s = int(input('Senha: '))

        while n != 'root' or s != 9090:
            print('Aesso negado. Tente novamente.')
            n = str(input('Nome de usuario: '))
            s = int(input('Senha: '))

        else:
            print(f'Bem vindo {n}!')
            # Aqui você pode adicionar códigos de outros programas para ser executado

        if cmd == 'sair':
            print('Saiu com sucesso.')
            break

if cmd == 'sair':
    print('Saiu com sucesso.')
