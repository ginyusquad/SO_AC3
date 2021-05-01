'''
Turma: CC3BN.

Integrantes: Claudia Thifany dos Santos (RA: 1903247);
             Gilberto Ramos de Oliveira (RA: 1903991);
             Leandro Epifanio Silva Costa (RA: 1902516);
             Rodrigo Monastero (RA: 1904247).

'''
from tabuleiro import Tabuleiro, JOGADOR_BOLINHA, JOGADOR_XIZINHO;
from threading import *;
import time;

class MeuSemaforo:
    # Tabuleiro
    jogo = Tabuleiro();
    # controlador
    controle = Semaphore(0)
    def verificaPosicao(self,x, y, jogador):
        # Solicitando inicio do uso da variavel compartilhada para a thread atual
        self.controle.acquire()
        return self.jogo.posicaoValida( x, y, jogador);
    # Joga um peça X ou O no tabuleiro
    def jogarPeca(self, x, y, jogador):
                
        self.jogo.colocarPeca( x, y, jogador)
        # Finalizando area de excução da thread atual para a proxima usar
        self.controle.release()

def Jogador(nome, simbolo):
    global semaforo;
    # loop da tread
    while True:
        while (not semaforo.jogo.existeVencedor()):
            print("Ainda não existe um ganhador! Vou jogar :)")
            # verificar se pode jogar
            #while <Condição de poder ou não jogar>:
                # Jogar
                # Verificar se alguem venceu
        time.sleep(4)

semaforo = MeuSemaforo();

jogador1 = Thread(target = Jogador, args = ('P1', JOGADOR_BOLINHA))
jogador2 = Thread(target = Jogador, args = ('P2', JOGADOR_XIZINHO))

jogador1.start();
jogador2.start();