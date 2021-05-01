# -*- coding: utf-8 -*-
# Números Primos felizes
JOGADOR_BOLINHA = 7;
JOGADOR_XIZINHO = 13;

class Tabuleiro:
    pecas = { 0:" - ",
              JOGADOR_BOLINHA:" O ",
              JOGADOR_XIZINHO:" X "
            };
    def __init__(self):
        self.estado = [[0,0,0],
                       [0,0,0],
                       [0,0,0]];
        self.lances = 0;
        self.ganhador = "";
    def posicaoValida(self, x, y, jogador):
        valido = False;
        #print("x:", x ,", y:",y,"jogador:",jogador);
        #print(self.estado);
        # verifica se o Simbolo passado e valido
        valido = jogador == JOGADOR_BOLINHA or jogador == JOGADOR_XIZINHO;
        # Verifica se a posição an matriz e valida
        valido = ( x >= 0 and x < 3 ) and ( y >= 0 and y < 3 );
        # Verifica se a posição já foi preenchida
        valido = self.estado[x][y] == 0;

        return valido;

    def colocarPeca(self, x, y, jogador):
        self.estado[x][y] = jogador;
        self.lances += 1;
        if (self.existeVencedor()):
            print(self.ganhador)

    def imprimir(self):
        retorno = "";
        for linha in self.estado:
            for coluna in linha:
                retorno += self.pecas[coluna];
            retorno +="\n";
        return retorno;

    def existeVencedor(self):
        if self.lances > 9:
            self.ganhador = ("ocorreu um empate!");
            return True;    
        existe = False;
        for peca in self.pecas:
            # Bloqueia a execução do 0
            if peca < 1:
                continue;
            else:
                soma = 0;
                # calcula linhas  horizontal X X X ou O O O
                for linha in self.estado:
                    soma = linha[0]+linha[1]+ linha[2];
                    if soma == peca * 3:
                        self.ganhador = "Temos um vencedor: " + self.pecas[peca];
                        return True;
                # calcula coluna                X O
                #                               X O
                #                               X O
                for coluna in range(0, 3):
                    soma = self.estado[0][coluna] + self.estado[1][coluna] + self.estado[2][coluna];
                    if soma == peca * 3:
                        self.ganhador = "Temos um vencedor: " + self.pecas[peca];
                        return True;
                # calcula vertical              X O O
                #                               O X O
                #                               O O X
                soma = self.estado[0][0] + self.estado[1][1] + self.estado[2][2];
                if soma == peca * 3:
                        self.ganhador = ("Temos um vencedor: " + self.pecas[peca]);
                        return True;
                # calcula vertical Direita      X X O
                #                               X O X
                #                               O X X
                soma = self.estado[0][2] + self.estado[1][1] + self.estado[2][0];
                if soma == peca * 3:
                    self.ganhador = ("Temos um vencedor: " + self.pecas[peca]);
                    return True;
        if self.lances > 8:
            self.ganhador = ("ocorreu um empate!");
            return True;
        return existe;
