'''Batalha naval :D'''


# importando as funções criadas
from funcoes import criarTabuleiro
from funcoes import mostrarRegras
from funcoes import colocarEmbarcacaoJogador
from funcoes import mostrarTabuleiro
from funcoes import colocarEmbarcacaoComputador
from funcoes import jogar


# construindo tabuleiros

# tabuleiro_jogador é o tabuleiro onde o jogador colocará seus barcos
# tabuleiro_computador é o tabuleiro onde o computador colocará seus barcos
# tabuleiro_apresentar é o tabuleiro que será apresentado para o jogador para ele saber onde já atirou

tabuleiro_jogador = criarTabuleiro()
tabuleiro_computador = criarTabuleiro()
tabuleiro_apresentar = criarTabuleiro()


# mostrar regras e instruções para o jogo
print(mostrarRegras())


# começar a posicionar as embarcações
print("Vamos começar a colocar as suas embarcações :)")
print("")


# primeiro mostra o tabuleiro
print("--- SEU TABULEIRO ---")
mostrarTabuleiro(tabuleiro_jogador)
print("")


# coloca as embarcações
colocarEmbarcacaoJogador(tabuleiro_jogador)


# o computador "escolhe" onde estará suas embarcações
colocarEmbarcacaoComputador(tabuleiro_computador)


# possivel teste
print("")
print("Ahhh... você pode testar o programa e ver o meu tabuleiro ;)")
print("")
print("(Digite 1 para sim ou qualquer outro caracter para não)")
print("")
teste = input("Você gostaria de ver? ")
print("")

# vai apresentar o mapa do adversário se o usuario digitar 1
if teste == "1":

    print("")
    print("--- TABULEIRO DO SEU ADVERSARIO")
    mostrarTabuleiro(tabuleiro_computador)
    print("")


print("")
print("Certo! Vamos começar :D")
print("")


# começar o jogo
jogar(tabuleiro_jogador, tabuleiro_computador, tabuleiro_apresentar)