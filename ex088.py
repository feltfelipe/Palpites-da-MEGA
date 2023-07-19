'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''
from random import randint
temp = []
jogos = []
palpites = int(input('Quantos palpites você quer? '))
for p in range(0, palpites):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont == 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
for i, p in enumerate(jogos):
    print(f'Jogo {i+1}: {p}')