def imprime(hotel):
    for linha in hotel:
        print(linha)

def fase_1():  # Função fase 1
    print('Bem vindo a fase 1')
    print('Na Fase 1, o jogador deve olocar o RATO e o GATO na seguinte matriz que representa os quartos:')
    imprime(hotel)
    pos_rato = int(input('Em qual posição quer olocar o RATO ?'))
    pos_gato = int(input('Em qual posição quer olocar o GATO ?'))
    if pos_rato == 6 and pos_gato == 3:
        print('Você Venceu a fase 1 !!!')
        fase_2()    # Caso usuário vença a fase 2 inicia
    else:
        print('Game Over!!!')

def fase_2():   # Função fase 2
    print('Bem vindo a fase 2 ')
    print('Na fase 2 o jogador deve olocar: CÃO, CÃO e OSSO: ')
    hotel_2 = [['-', '*', '*', '*'], ['*', 'C', '-', '-']]
    imprime(hotel_2)
    pos_cao = int(input('Em qual posição quer olocar o CÃO ?'))
    pos_cao_2 = int(input('Em qual posição quer olocar o CÃO ?'))
    pos_osso = int(input('Em qual posição quer olocar o OSSO ?'))
    if pos_cao == 7 or pos_cao == 8 or pos_cao_2 == 7 or pos_cao_2 == 8 and pos_osso == 1:
        print('Você Venceu a fase 2 !!!')
        fase_3()    # Caso usuário vença inicia a fase 3
    else:
        print('Game Over !!!')

def fase_3():    # Função fase 3
    print('Bem Vindo a fase 3 ')
    print('Na fase 3 o jogador deve olocar: GATO, RATO E OSSO ')
    hotel_3 = [['-', '*', '*', '*'], ['-', 'G', '-', '*']]
    imprime(hotel_3)
    pos_gato = int(input('Em qual posição quer olocar o GATO ?'))
    pos_rato = int(input('Em qual posição que olocar o RATO ?'))
    pos_osso = int(input('Em qual posição quer olocar o OSSO ?'))
    if pos_rato == 1 and pos_osso == 5 and pos_gato == 7:
        print('Você Venceu a fase 3 !!!!')
        fase_4()   # Caso usuário vença inicia a fase 4
    else:
        print('Game Over !!!')

def fase_4():   # Função fase 4
    print('Bem Vindo a fase 4 ')
    print('Na fase 4 o jogador deve olocar: QUEIJO, QUEIJO, E OSSO ')
    hotel_4 = [['-', '-', '-', '*'], ['*', 'R', '*', '*']]
    imprime(hotel_4)
    pos_queijo = int(input('Em qual posição quer olocar o QUEIJO ?'))
    pos_queijo_2 = int(input('Em qual posiçao quer olocar o QUEIJO ?'))
    pos_osso = int(input('Em qual posição quer olocar o OSSO ?'))
    if pos_osso == 2:
        if pos_queijo == 1 or pos_queijo == 3 and pos_queijo_2 == 1 or pos_queijo_2 == 3:
            print('Você Venceu o Jogo !!!!!')
    else:
        print('Game Over !!!')

#Programa principal

hotel = [['*', '*', '-', 'G' ], ['R', '-', '*', '*']]
inicio = ('-' * 10 + 'Hotel dos Animais' + '-' * 10)
print(inicio)
print('Especificando Posição:')
print('[1,2,3,4]')
print('[5,6,7,8]')
fase_1()

