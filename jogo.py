#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Turma: CC3BN.

Integrantes: Claudia Thifany dos Santos (RA: 1903247);
             Gilberto Ramos de Oliveira (RA: 1903991);
             Leandro Epifanio Silva Costa (RA: 1902516);
             Rodrigo Monastero (RA: 1904247).

'''
from tabuleiro import Tabuleiro, JOGADOR_BOLINHA, JOGADOR_XIZINHO;
from threading import *;
import random;
import time;

class MeuSemaforo:
    # Tabuleiro
    jogo = Tabuleiro();
    # controlador começando aberto
    controle = Semaphore(1);
    # Joga um peca X ou O no tabuleiro
    def jogarPeca(self, nome, jogador):
        self.controle.acquire();
        if (self.jogo.existeVencedor()):
            self.controle.release();
            return;
        print("\n"+nome+" "+self.jogo.pecas[jogador]+" pensando....")
        # verificar se pode jogar
        x = random.randrange(0, 2);
        y = random.randrange(0, 2);
        while not self.jogo.posicaoValida( x, y, jogador):
            x = random.randrange(0, 3);
            y = random.randrange(0, 3);
            time.sleep(1);
        print("Jogada do "+ nome+" "+self.jogo.pecas[jogador])
        self.jogo.colocarPeca( x, y, jogador)
        # Finalizando area de excução da thread atual para a proxima usar
        self.controle.release();
        print(self.jogo.imprimir());

def Jogador(nome, simbolo):
    global semaforo;
    # loop da tread
    while True:
        while (not semaforo.jogo.existeVencedor()):
            time.sleep(1);
            # CHama o semaforo para verificar e executar a jogada caso ninguem esteja jogando no momento
            semaforo.jogarPeca(nome, simbolo); # Jogar
        else:

            return 0;
            # verifica se alguem venceu
    time.sleep(1)

semaforo = MeuSemaforo();

jogador1 = Thread(target = Jogador, args = ('Jogador 1', JOGADOR_BOLINHA))
jogador2 = Thread(target = Jogador, args = ('Jogador 2', JOGADOR_XIZINHO))

jogador1.start();
jogador2.start();
