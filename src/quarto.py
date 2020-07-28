# patricia.adda.quarto.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo de Tabuleiro Quarto.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Classes neste módulo:

    :py:class:`JogoDoQuarto` Jogo de tabuleiro para dois jogadores.

    :py:class:`Pino` Representa um pino que se move de um tabuleiro para outro.

    :py:class:`Casa` Representa um case que pode receber um pino no tabueiro.


Changelog
---------
.. versionadded::    20.07
        Criando o tabuleiro.

.. versionadded::    20.07.01
        Criando Pino e Casa.

"""
from vitollino.main import Cena, Elemento, STYLE
from browser.html import SPAN
TAMANHO = 600
STYLE.update(width=TAMANHO, height=f"{TAMANHO}px")


class Pino(Elemento):
    """ Pinos do jogo quarto variando em cor, altura, forma e buraco

        Observação: Uma *folha sprite* é uma imagem contendo vários desenhos com peças
        que serão usados em um jogo.

        :param indice: O índice do pino na *folha sprite* (cada imagem tem 8 pinos).
        :param cor: Nome da imagem sprite com um conjunto de pinos claros ou escuros.
        :param casa: Casa original onde o pino vai ser colocado.
        :param dx: o intervalo horizontal em pixels entre duas figuras de pino na *folha sprite*.
        :param dy: o intervalo vertical em pixels entre duas figuras de pino na *folha sprite*.
    """
    PINOS = {}  # Coleção de todos pinos criados, serve para localizar um pino dado o nome.
    # COR é o dicionário com duas *folhas sprite* de pinos colocados no topo e no lado.
    COR = dict(topo="https://imgur.com/Wo6skC7.png", lado="https://imgur.com/chvIdvJ.png")
    MOD = dict(topo=2, lado=4)  # Número de figuras por linha em cada *folha sprite*.
    def __init__(self, indice, cor, casa, dx=101, dy=60):
        pino, modulo = self.COR[cor], self.MOD[cor]
        x, y, nome = indice // modulo * dx , (indice % modulo) * dy, f"{cor}{indice}"
        super().__init__(pino, x=8, y=-2, w=dx, h=dy, cena=casa, tipo="auto", tit=nome, drag=True,
        style={"background-position": f"{-x}px {-y}px"})
        self.PINOS[nome] = self  # adiciona este pino criado aqui (self) no dicionário de pinos.

    @staticmethod
    def pino(nome):
        """ Retorna o pino localizado dado o nome.

            :param nome: O nome do pino no dicionário de pinos *PINOS*.
            :return: O objeto pino que tem o nome dado.
            :rtype: Instância da classe Pino.
        """
        return Pino.PINOS[nome]

    @staticmethod
    def pinos(cor, table):
        """ Cria um conjunto de pinos de uma cor e aloca no dado tabuleiro.

            :param table: A tabela contendo um cojunto de casas onde os pinos serão alocados.
            :param cor: Nome da imagem sprite com um conjunto de pinos claros ou escuros.
            :return: Uma lista de pinos alocados nas casas do tabuleiro dado.
            :rtype: Lista contendo instâncias da classe Pino.
        """
        casas = enumerate([casa for linha in table for casa in linha])
        return [Pino(indice, cor, casa) for indice, casa in casas]


class Casa(Elemento):
    """ Casa do jogo quarto, podendo ser do tabuleiro central ou adjacentes.

        :param base: A cena em que este tabuleiro vai entrar.
        :param fundo: A imagem que representa esta casa.
        :param livre: Indica se a casa está livre ou ocupada quando for criada.
        :param t: Tamanho (altura e largura do desenho da casa, inicia em um oitavo do tabuleiro.
        :param x: A posição absoluta horizontal em casas que esta casa vai ser colocada.
        :param y: A posição absoluta vertical em casas que esta casa vai ser colocada.
        :param dx: O deslocamento horizontal em casas que esta casa tem em relação à esquerda.
        :param dy: O deslocamento vertical em casas que esta casa tem em relação ao topo.
        :param mx: Ajuste fino horizontal em pixels do posicionamento da casa.
        :param my: Ajuste fino vertical em pixels do posicionamento da casa.

        .. note::

            :folha sprite: é uma imagem contendo vários desenhos com peças
                que serão usados em um jogo.

            :dropper: dicionário necessário para definir o comportamento do drop.
                Cada chave deste dicionário deve ser o nome de um pino passível de
                ser arrastado para esta casa. Os nomes são do tipo *topo0 ... topo7*
                ou *lado0 ... lado7*. A construção *{f"{nome}{pino}": ..}* é chamada
                em Python de dict comprehension, pois gera um dicionário a partir de
                uma iteração. O termo *f"{nome}{pino}"* constrói as chaves do dicionário
                a partir da lista (topo, lado) e dos números de 0 a 7. O termo
                *lambda ev, nome_pino, \*_: self.entrar(nome_pino)* é uma função anônima
                que recebe os parametros *ev* e *nome_pino* enviados pelo mecanismo interno
                de arrasto do Elemento. Neste caso, para qualquer pino eu quero que ele
                entre na casa corrente, por isso o *self.entrar(nome_pino)* é chamado dentro
                da função anônima.

    """
    def __init__(self, base, fundo, x, y, dx=0, dy=3, mx=0, my=0, livre=False, t=TAMANHO // 8):
        x, y = t * (x + dx) + mx, t * (y + dy) - my
        dropper = {f"{nome}{pino}": lambda ev, nome_pino, *_: self.entrar(nome_pino)
                    for nome in ("lado", "topo") for pino in range(8)}
        super().__init__(fundo, x=x, y=y, w=t, h=t, cena=base, drop=dropper)
        self.livre = livre

    def entrar(self,nome):
        """ Permite um pino entrar nesta casa se ela estiver livre.

            :param nome: O nome do pino que vai entrar na casa.
        """
        Pino.pino(nome).entra(self) if self.livre else None
        self.livre = False


class JogoDoQuarto:
    """ Jogo do Quarto - Jogo de Tabuleiro.
    Quarto é um jogo de tabuleiro para dois jogadores inventado pelo matemático suíço Blaise Müller em 1991.

    O jogo é jogado em um tabuleiro 4 × 4. Existem 16 peças únicas para brincar, cada uma das quais é:

    - alto ou baixo;
    - vermelho ou azul (ou um par diferente de cores, por exemplo, madeira manchada de clara ou escura);
    - quadrado ou circular; e
    - topo oco ou topo sólido.

    Os jogadores se revezam na escolha de uma peça que o outro jogador deve colocar no tabuleiro.
    Um jogador vence colocando uma peça no tabuleiro que forma uma linha horizontal,
    vertical ou diagonal de quatro peças, todas com um atributo em comum
    (todas curtas, todas circulares, etc.). Uma regra de variante incluída em muitas edições
    fornece uma segunda maneira de ganhar colocando quatro peças correspondentes em um quadrado 2 × 2.

    """
    MADEIRA = "https://i.imgur.com/8mPjfYk.jpg"  # Textura do fundo do jogo.
    TABULEIRO = "https://i.imgur.com/yPFsdKw.png"  # Desenho da casa no tabuleiro central.
    MINITAB = "https://i.imgur.com/DjKe0KY.png" # Desenho da casa no tabuleiro adjacente.
    def __init__(self):
        self.lado = TAMANHO // 8
        self.tabuleiro = Cena(self.MADEIRA)
        margin = self.lado // 3
        self.tabua = self.table(self.tabuleiro, self.TABULEIRO, mx=margin, my=margin, livre=True)
        mx, my = self.lado//3, 0.66 * self.lado
        self.tab_topo = self.table(self.tabuleiro, self.MINITAB, 2, 4, 0, 1, 50, 50)
        self.tab_lado = self.table(self.tabuleiro, self.MINITAB, 4, 2, 5, 4, 50, 60)
        self.pin_topo = Pino.pinos("topo", self.tab_topo)
        self.pin_lado = Pino.pinos("lado", self.tab_lado)  # , dy=101.5)

    def vai(self):
        """ Aloca esta cena na página do navegador.
        """
        self.tabuleiro.vai()

    def table(self, base, fundo, linhas=5, colunas=5, dx=0, dy=3, mx=0, my=0, livre=False):
        """ Cria um conjunto de casas de um tipo e aloca na cena dada.

            :param base: A cena em que este tabuleiro vai entrar.
            :param fundo: A imagem que representa cada casa.
            :param livre: Indica se as casas estão livres ou ocupadas quando forem criadas.
            :param t: Tamanho (altura e largura do desenho da casa, inicia em um oitavo do tabuleiro.
            :param linhas: O número de linhas de casas neste tabuleiro.
            :param colunas:  O número de colunas de casas neste tabuleiro.
            :param dx: O deslocamento horizontal em casas que cada casa tem em relação à esquerda.
            :param dy: O deslocamento vertical em casas que cada casa tem em relação ao topo.
            :param mx: Ajuste fino horizontal em pixels do posicionamento de cada casa.
            :param my: Ajuste fino vertical em pixels do posicionamento de cada casa.
            :return: Uma tabela de duas dimensões de casas arranjadas nas posições dadas.
            :rtype: Lista de listas contendo instâncias da classe Casa.
        """
        return [[Casa(base, fundo, i, j, dx, dy, mx, my, livre)
                for j in range(linhas)] for i in range(colunas)]


if __name__ == "__main__":
    JogoDoQuarto().vai()
