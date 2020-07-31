import pygame
from random import randint 

# Var de trainamento
# Lista de saida [Esquerda, Cima, Direita, Baixo]
listaOutput = [0,0,0,0]

# Lista de entrada [n da rodada ,pontos obtidos
# matriz do tabuleiro] (tabuleiro incluindo 
# paredes, corpo da cobra e maca)
listaEntrada = [0]*3

# Nota: a matriz sera quase 4 vezes maior que o
# tabuleiro em si para a cebeca ser centralizada
# e poder enxergar o tabuleiro inteiro sempre
tamanho_tabuleiro_maior = 20 + 19
matriz_do_tabuleiro = [0]*tamanho_tabuleiro_maior
for i in range(20):
    matriz_do_tabuleiro[i] = [0]*39

listaEntrada[2] = matriz_do_tabuleiro

# Funcoes para inserir a cabeca e o corpo
def corpoFunc(x, y):
    screen.blit(imagemCorpo, (x,y))

def cabecaFunc(x, y):
    screen.blit(imagemCabeca, (x,y))

# Funcao para inserir quadrado verde do fundo
def quadradoFundoFunc(x, y):
    screen.blit(imagemQuadradoFundo, (x,y))

# Funcao para inserir a maca
def macaFunc(x, y):
    screen.blit(imagemMaca, (x,y))

# Funcao para placar
def placarFunc(x,y):
    placar = font.render("Pontos: " + str(pontos), True, (255, 255, 255))
    screen.blit(placar, (x,y))


# Loop de treino
for c in range (2):

    # Inicializa o pygame
    pygame.init()

    # Cria tela e define tamanho
    screen = pygame.display.set_mode((600,600))

    # Titulo e icone
    pygame.display.set_caption("Jogo da Cobrenha de ThurMP")
    icone = pygame.image.load("snake icon.png")
    fim_de_jogo = False
    rodada = 0

    # Define fonte
    pontos = 0
    font = pygame.font.Font('freesansbold.ttf', 32)

    # Cria e atualiza fundo
    background = pygame.image.load("fundo_quadriculado_verde.png")
    screen.blit(background,(0,0))

    # Load das imagens
    imagemCorpo = pygame.image.load("corpo.png")
    imagemCabeca = pygame.image.load("cabeça_direita.png")
    imagemQuadradoFundo = pygame.image.load("quadrado_do_fundo.png")
    imagemMaca = pygame.image.load("maca1.png")

    # Configuracao inicial da cabeca
    cabecaX = 181
    cabecaY = 271


    #for i in range(39):
    #    matriz_do_tabuleiro[(macaY-1)//30][(macaX-1)//30] = 


    # Jogo comeca indo para a direita
    cabecaXChange = 30
    cabecaYChange = 0

    # Listas para manter armazenadas as posicoes do corpo
    # (Ja com a configuracao inicial)
    listaXCorpo = [91, 121 ,151]
    listaYCorpo = [271, 271, 271]

    # Configuracao inicial do corpo
    cabecaFunc(cabecaX, cabecaY)
    corpoFunc(91, 271)
    corpoFunc(121, 271)
    corpoFunc(151, 271)

    matriz_do_tabuleiro[(271-1)//30][(91-1)//30] = -1
    matriz_do_tabuleiro[(271-1)//30][(121-1)//30] = -1
    matriz_do_tabuleiro[(271-1)//30][(151-1)//30] = -1

    # Cria a primeira maca e garante que nao esta na cobra
    macaY = (randint(0,19)*30)+1
    macaX = (randint(0,19)*30)+1
    while((macaX in listaXCorpo) and (macaY in listaYCorpo)):
        macaY = (randint(0,19)*30)+1
        macaX = (randint(0,19)*30)+1
    macaFunc(macaX, macaY)
    matriz_do_tabuleiro[(macaY-1)//30][(macaX-1)//30] = 1

    # Var para verificar se a cobra deve crescer ou nao
    crescer = False
    pygame.time.wait(1000)


    # Game Loop
    running = True
    while running:
        
        # Setando a Lista de entrada 
        listaEntrada[0] = rodada
        listaEntrada[1] = pontos
        #listaEntrada[2] = matriz_do_tabuleiro
        #listaEntrada[2] = (macaX-1)/30
        #listaEntrada[3] = (macaY-1)/30
        #listaEntrada[4] = (cabecaX-1)/30
        #listaEntrada[5] = (cabecaY-1)/30
        
        # Get dos eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Se alguma seta for apertada 
            if event.type == pygame.KEYDOWN:
                rodada += 1
                if not fim_de_jogo and rodada > 1:
                    # Nota: nao muda de direcao caso ja esteja indo para a desejada
                    if (event.key == pygame.K_LEFT) and (cabecaXChange == 0): 
                        imagemCabeca = pygame.image.load("cabeça_esquerda.png")
                        cabecaXChange = -30
                        cabecaYChange = 0

                    if (event.key == pygame.K_RIGHT) and (cabecaXChange == 0):
                        imagemCabeca = pygame.image.load("cabeça_direita.png")
                        cabecaXChange = 30
                        cabecaYChange = 0

                    if (event.key == pygame.K_DOWN) and (cabecaYChange == 0):
                        imagemCabeca = pygame.image.load("cabeça_baixo.png")
                        cabecaXChange = 0
                        cabecaYChange = 30

                    if (event.key == pygame.K_UP) and (cabecaYChange == 0):
                        imagemCabeca = pygame.image.load("cabeça_cima.png")
                        cabecaXChange = 0
                        cabecaYChange = -30

        if rodada>0:
            # Se a maca for pega, add 1 ponto e cria outra
            # Atuliza a posicao da da maca na matriz
            if (cabecaX == macaX and cabecaY == macaY):
                matriz_do_tabuleiro[(macaY-1)//30][(macaX-1)//30] = 0
                pontos += 1
                macaY = (randint(0,19)*30)+1
                macaX = (randint(0,19)*30)+1
                matriz_do_tabuleiro[(macaY-1)//30][(macaX-1)//30] = 1

                # Garante que a maca nao apareca em cima da cobra
                while((macaX in listaXCorpo) and (macaY in listaYCorpo)):
                    macaY = (randint(0,19)*30)+1
                    macaX = (randint(0,19)*30)+1
                macaFunc(macaX, macaY)
                # Guarda o valor para ela crescer
                crescer = True

            # Coloca o corpo logo onde a cabeca sai e
            # grava na lista
            listaXCorpo.append(cabecaX)
            listaYCorpo.append(cabecaY)

            matriz_do_tabuleiro[(cabecaY-1)//30][(cabecaX-1)//30] = -1

            corpoFunc(cabecaX, cabecaY)
            cabecaX += cabecaXChange
            cabecaY += cabecaYChange



            # Condicao de cobra bater na borda
            if (cabecaX < 0) or (cabecaX > 600) or (cabecaY > 600) or (cabecaY < 0):
                # Plot do placar
                placarFunc(210,270)
                cabecaXChange = 0
                cabecaYChange = 0
                fim_de_jogo = True

            # Condicao de cobra bater nela mesma
            for i in range(len(listaXCorpo)):
                if(cabecaX == listaXCorpo[i]): 
                    if (cabecaY == listaYCorpo[i]):
                        # Plot do placar
                        placarFunc(210,270)
                        cabecaXChange = 0
                        cabecaYChange = 0
                        fim_de_jogo = True
                
            # Cobre a ponta da cauda com quadrado verde
            # Caso crescer == True faz a cobra crescer 1 espaco
            if not crescer:
                matriz_do_tabuleiro[(listaYCorpo[0]-1)//30][(listaXCorpo[0]-1)//30] = 0
                quadradoFundoFunc(listaXCorpo.pop(0), listaYCorpo.pop(0))
            crescer = False

            # Coloca a cabeca no espaco seguinte
            cabecaFunc(cabecaX, cabecaY)

        # Atualiza a tela e gera delay
        pygame.display.update()
        pygame.time.wait(150)
