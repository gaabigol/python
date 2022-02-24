from random import randint#função importada para gerar números aleatórios

def cadastrar():# Função para armazenar os dados do usuário cadastrado
    nome = input('Digite seu nome:')
    email = input('Digite seu email:')
    telefone = input('Digite seu telefone:')
    curso = input('Digite seu curso:')
    voucher = randint(100, 400)
    cadastro['nome'] = nome
    cadastro['email'] = email
    cadastro['telefone'] = telefone
    cadastro['curso'] = curso
    cadastro['voucher'] = voucher
    lista.append(cadastro.copy())
cadastro = {}
lista = []
#Programa principal
while True:
    inicio = ('*' * 22 + 'Menu' + '*' * 22)
    print(inicio)
    print('1 - Nova inscrição')
    print('2 - Visualizar inscrição')
    print('0 - Encerrar')
    #neste bloco de verificação optei por verificar strings pois caso seja digitado qualquer outro caractere o programa
    #irá apresentar a mensagem de erro e repetira a pergunta ao usuário
    op = input('Opção escolhida:')
    if op == '1':
        cadastrar()
    if op == '2':
        if lista:#Verifica se a na lista encontra se algum usuário cadastrado ou se esta vazia
            for e in lista:
                for i, j in e.items():
                    print('{} : {}'.format(i, j))
                print('-' * 20)
        else:
            print('nenhuma inscrição cadastrada')
    if op == '0':
        print('Encerrando')
        break
    else:
        if op != '1' and op != '2' and op != '0':
            print('Erro digite uma opção válida!')
            continue

