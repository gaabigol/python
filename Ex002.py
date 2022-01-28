
while True:#loop infinito para que o programa só encerre quando o usuário quiser

#Bloco de entrada de dados tais como informação do usuário
    nome = input('Por favor, Informe o nome da criança:')
    idade = int(input('Por favor, Informe a idade:'))

#Bloco de verificação de idades e classificação de turmas
    if idade <= 5:
        print('O aluno(a) {} tem {} anos e está no ensino infantil'.format(nome, idade))

    elif idade <= 10:
        print('O aluno(a) {} tem {} anos e está no ensino fundamental I'.format(nome, idade))

    elif idade <= 14:
        print('O aluno(a) {} tem {} anos e está no ensino infantil II'.format(nome, idade))

    elif idade >= 15:
        print('O aluno(a) {} tem {} anos e está no ensino médio'.format(nome, idade))
#neste bloco verificamos se o usuário deseja continuar o programa ou encerrar
    opcao = input('Deseja continuar?  0 - Não  1 - Sim')

    if opcao == '1':
        continue
    if opcao == '0':
        break

