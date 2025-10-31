'''funções'''

# para colocar as embarcações aleatórias do computador
import random

# para dar emoção de esperar a jogada do computador
import time


def criarTabuleiro():
    """Função para criar um tabuleiro (10x10)"""

    return [[" " for i in range(10)] for i in range(10)]


def mostrarRegras():
    """Função para mostrar as regras"""

    print("--- BATALHA NAVAL ---")
    print("")
    print("Bem-vindo(a) ao jogo de BATALHA NAVAL:D")
    print("")
    print("Essas são as instruções para o jogo: ")
    print("- Você jogará contra mim, o computador :)")
    print("- Cada jogador terá 5 embarcações, cada uma delas ocupando uma única posição no tabuleiro.")
    print("- No inicio da partida, você deve determinar as posições das suas embarcações ( eu vou fazer isso também ;) ).")
    print("- Cada jogador tem 1 tiro por vez, caso esse tiro acerte uma embarcação, você ( ou eu :3 ) terá o direito de dar outro tiro.")
    print("- O vencedor será aquele que conseguir afundar todas as embarcações do adversário")
    print("")
    print("Boa sorte e se divirta XD")
    print("")


def colocarEmbarcacaoJogador(tabuleiro_jogador):
    """
    Função para colocar as embarcações do jogador no tabuleiro
    
    São 5 embarcações que ocupam 1 espaço cada
    Cada embarcação será vista no tabuleiro como '^'

    """

    print("--- informações necessárias ---")
    print("- X: coordenada vertical")
    print("- Y: coordenada horizontal")
    print("")
    

    # número de embarcações que já foram colocadas pelo usuário
    colocado = 1


    # até atingir o número maximo de embarcações(que é 5)
    while colocado < 6:
        

        # para tentar até dar certo a inserção
        while True:


            # try para tratamento dos dados de entrada
            try:


                print(f"Digite a posição da sua embarcação {colocado}: ")

                # le a posição da embarcação
                x = int(input("X: "))
                y = int(input("Y: "))


                # se a posição estiver vazia ele insere
                if tabuleiro_jogador[x][y] == " ":

                    tabuleiro_jogador[x][y] = "^"

                    # contador de quantas embarcações foram colocadas aumenta
                    colocado = colocado + 1
                    
                    # mostra como está o tabuleiro
                    print("--- SEU TABULEIRO ---")
                    print("")
                    print(mostrarTabuleiro(tabuleiro_jogador))
                    print("")
                    
                    break
                
                # se não estiver vazia ele solicita outra
                else:

                    print("Essa posição já está ocupada. Tente outra ;)")

                    # e mostra como o tabuleiro está
                    print("--- SEU TABULEIRO ---")
                    print("")
                    print(mostrarTabuleiro(tabuleiro_jogador))
                    print("")


            # tratamento de erros
            except (ValueError, IndexError):

                print("Entrada inválida. Por favor, insira números inteiros até 9.")
                print("")


def mostrarTabuleiro(tabuleiro):
    """Função para mostrar o tabuleiro"""
    
    # indica as coordenadas de y
    print("  0 1 2 3 4 5 6 7 8 9")
    
    # for para apresentar linha por linha
    for i, linha in enumerate(tabuleiro):
        
        # i é equivalente a coordenada x
        print(f"{i}|" + " ".join(linha))


def colocarEmbarcacaoComputador(tabuleiro_computador):
    """
    Função para colocar as embarcações do computador
    
    Usa o random para "escolher" o posicionamento das embarcações (de forma aleatória, claro)
    São 5 embarcações que ocupam 1 espaço cada
    Cada embarcação será vista no tabuleiro como '^'
    """


    colocado = 0

    while colocado < 5:

        # escolhe aleatoriamente as coordenadas da embarcação
        # a função recebe como parametro os número possiveis (de 0 a 9)

        x = random.randint(0, len(tabuleiro_computador) - 1)
        y = random.randint(0, len(tabuleiro_computador[0]) - 1)


        # só coloca o ^ e aumenta o contador se a casa estiver disponível
        if tabuleiro_computador[x][y] == " ":

            tabuleiro_computador[x][y] = "^"

            colocado += 1
                    
        
def jogar(tabuleiro_jogador, tabuleiro_computador, tabuleiro_apresentar):
    """
    Função para inciar o jogo

    A função fica em loop até algum dos jogadores fazer 5 pontos (acertar os 5 barcos).
    Após cada jogada, será mostrado a situação atual do tabuleiro do jogador e o tabuleiro que contém as tentativas dele 
    """

    # ambos começam com 0 pontos
    jogador_pts = 0
    computador_pts = 0     

    # o usuario começa a jogar primeiro
    print("Você começa :)")
    print("")   

    while True:

        try:

            # enquanto os jogadores não acertarem as 5 embarcações
            while jogador_pts < 5 and jogador_pts < 5:


                # primeiro o usuario joga

                # inserir as coordenadas de ataque
                print("Digite a posição que você deseja atacar: ")
                x_atqJ = int(input("X: "))
                y_atqJ = int(input("Y: "))


                # se ele ja tiver tentado essa casa (caso tenha errado)
                if tabuleiro_apresentar[x_atqJ][y_atqJ] == "-":

                    print("")

                    # ele pode tentar outra casa
                    print("Você já tentou essa casa! Tente outra ;)")
                    continue 

                # se ele ja tiver tentado essa casa (caso tenha acertado)
                elif tabuleiro_apresentar[x_atqJ][y_atqJ] == "X":

                    print("")

                    # ele pode tentar outra casa
                    print("Você já tentou essa casa! Tente outra ;)")
                    continue 


                # se for uma casa que ele nunca tentou
                else:

                    # se tiver uma embarcação no local
                    if tabuleiro_computador[x_atqJ][y_atqJ] == "^":

                        # aumenta o número de pontos do jogador
                        jogador_pts = jogador_pts + 1

                        # apresenta pro usuario que ele acertou
                        print("")
                        print("BOAAA!! você acertou um barco :D")

                        # deixa um X onde o jogador acertou a embarcação (no tabuleiro de apresentação)
                        tabuleiro_apresentar[x_atqJ][y_atqJ] = 'X'
                
                        # o jogador continua a jogada
                        print("Pode jogar de novo ;)")

                        # mostra como está o tabuleiro onde o usuario esta tentando acertar (suas tentaivas)
                        print("")
                        print("--- TABULEIRO DO SEU ADVERSÁRIO ---")
                        mostrarTabuleiro(tabuleiro_apresentar)


                        continue
                
                
        
                    # se ele errar
                    else:

                        # avisa que não acertou
                        print("Poxaa você não acertou :(")

                        # muda no tabuleiro de apresentação
                        tabuleiro_apresentar[x_atqJ][y_atqJ] = '-'

                        # mostra como está o tabuleiro onde o usuario esta tentando acertar (suas tentativas)
                        print("")
                        print("--- TABULEIRO DO SEU ADVERSÁRIO ---")
                        mostrarTabuleiro(tabuleiro_apresentar)




                # vez do computador jogar

                print("")
                print("É a minha vez agora :D")
        
                # tempo pra "pensar"
                time.sleep(2) 

                
                continuar = 0


                # para ele funcionar enquanto o computador acertar
                while continuar == 0:
            
                    # "escolhe" as coordenadas do tiro
                    x_atqC = random.randint(0, len(tabuleiro_jogador) - 1)
                    y_atqC = random.randint(0, len(tabuleiro_jogador[0]) - 1)


                    # caso de a mesma coordenada (já tenha "escolhido" e errado)
                    if tabuleiro_jogador[x_atqC][y_atqC] == "-":
                        
                        # o computador tenta novamente
                        continue
                    

                    # caso de a mesma coordenada (já tenha "escolhido" e acertado)
                    elif tabuleiro_jogador[x_atqC][y_atqC] == "X":

                        # o computador tenta novamente
                        continue

                    # se for uma casa que ele nunca "escolheu"
                    else:
        
                        # mostra pro usuário qual foi as coordenadas escolhidas
                        print("")
                        print(f"Eu escolhi as coordenadas ({x_atqC}, {y_atqC})")


                        # se o computador acertou
                        if tabuleiro_jogador[x_atqC][y_atqC] == '^':

                            # o número de pontos aumenta
                            computador_pts = computador_pts + 1

                            # altera o tabuleiro do usuario
                            tabuleiro_jogador[x_atqC][y_atqC] = 'X'

                            # avisa que acertou a embarcação
                            print("")
                            print("Acertei uma embarcação sua!! XD")

                            # mostra como está o atual tabuleiro do jogador
                            print("")
                            print("--- SEU TABULEIRO ---")
                            mostrarTabuleiro(tabuleiro_jogador)

                            # avisa que vai tentar novamente, pois acertou a embarcação
                            print("")
                            print("Vou tentar de novo ;)")

                            # continua tentando até errar
                            continue


                        # se não tiver uma embarcação onde ele "escolheu"
                        else:

                            # modifica o tabuleiro do usuario
                            tabuleiro_jogador[x_atqC][y_atqC] = '-'

                            # avisa que errou
                            print("")
                            print("Errei :(")

                            # modifica para sair do loop
                            continuar = 1

                            # mostra o tabuleiro atual do jogador
                            print("")
                            print("--- SEU TABULEIRO ---")
                            mostrarTabuleiro(tabuleiro_jogador)


                # volta para 0 para funcionar no próximo turno 
                continuar = 0


            # se o usuario ganhar
            if jogador_pts == 5:

                print("")
                print("PARABENS! Você ganhou XD")

            # se o computador ganhar
            else:
        
                print("")
                print("Eu ganhei!!")
                print("Não foi dessa vez pra você :(")


        # trata erro de entrada
        except (ValueError, IndexError):

            print("Entrada inválida. Por favor, insira números inteiros até 9.")
            print("")

    