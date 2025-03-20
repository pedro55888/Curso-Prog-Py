import pygame #biblioteca de jogos
import random #bibliotecapara gerar valores randomicos 

# Inicializa o pygame
pygame.init()

# Define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Define o tamanho da janela
LARGURA = 800 #largura da tela
ALTURA = 600 #altura da tela
tela = pygame.display.set_mode((LARGURA, ALTURA)) #cria a tela com os tamanhos definidos
pygame.display.set_caption("Pong") #adiciona o nome na barra da tela

# Define o FPS (frames por segundo)
FPS = 60 #frames por segundo padrão do jogo
clock = pygame.time.Clock() #usado para controlar a taxa de atualização da tela.

# Define o tamanho e a velocidade das barras e da bola
largura_barra = 10 #largura da barra
altura_barra = 100 #altura da barra
velocidade_barra = 10 #velocidade da barra
tamanho_bola = 20 #tamanho da bola
velocidade_bola_x = 5 * random.choice((1, -1)) # define velocidade inicial e posicao da bola, se for positivo move pro lado direito e negativo lado esquerdo
velocidade_bola_y = 5 * random.choice((1, -1)) # define velocidade inicial e posicao da bola, se for positivo move pro lado direito e negativo lado esquerdo

# Posições iniciais
x_barra_esquerda = 50 #A coordenada horizontal (eixo X) da barra esquerda é definida como 50 pixels a partir da borda esquerda da tela.
y_barra_esquerda = ALTURA // 2 - altura_barra // 2 #A coordenada vertical (eixo Y) da barra esquerda é definida como a metade da altura da tela (ALTURA // 2) menos a metade da altura da própria barra (altura_barra // 2).

x_barra_direita = LARGURA - 50 - largura_barra #A coordenada horizontal (eixo X) da barra direita é definida como a largura total da tela (LARGURA) menos 50 pixels (para dar um espaço entre a borda e a barra) e a largura da própria barra (largura_barra).
y_barra_direita = ALTURA // 2 - altura_barra // 2 #Assim como para a barra esquerda, a coordenada vertical (eixo Y) da barra direita é definida como a metade da altura da tela (ALTURA // 2) menos a metade da altura da própria barra (altura_barra // 2).

x_bola = LARGURA // 2 - tamanho_bola // 2 #A coordenada horizontal (eixo X) da bola é definida como a metade da largura da tela (LARGURA // 2) menos a metade do tamanho da bola (tamanho_bola // 2). Isso posiciona a bola no centro horizontal da tela.
y_bola = ALTURA // 2 - tamanho_bola // 2 #A coordenada vertical (eixo Y) da bola é definida como a metade da altura da tela (ALTURA // 2) menos a metade do tamanho da bola (tamanho_bola // 2). Isso posiciona a bola no centro vertical da tela.

# Função para desenhar elementos na tela
def desenhar_jogo():
    tela.fill(PRETO) #background da tela
    pygame.draw.rect(tela, BRANCO, (x_barra_esquerda, y_barra_esquerda, largura_barra, altura_barra)) #desenha barra esquerdda
    pygame.draw.rect(tela, BRANCO, (x_barra_direita, y_barra_direita, largura_barra, altura_barra)) #desenha barra direira
    pygame.draw.ellipse(tela, BRANCO, (x_bola, y_bola, tamanho_bola, tamanho_bola)) #desenha bola
    pygame.draw.aaline(tela, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA)) #desenha a linha central
    pygame.display.flip() #atualiza o conteúdo da tela

# Função para mover a bola
def mover_bola():
    global x_bola, y_bola, velocidade_bola_x, velocidade_bola_y #declara as variáveis x_bola, y_bola, velocidade_bola_x e velocidade_bola_y como globais.
    x_bola += velocidade_bola_x
    y_bola += velocidade_bola_y
    #Essas duas linhas atualizam as coordenadas da bola (x_bola e y_bola) com base em suas velocidades horizontais e verticais (velocidade_bola_x e velocidade_bola_y). Isso faz a bola se mover pelo campo de jogo.

    if y_bola <= 0 or y_bola >= ALTURA - tamanho_bola: #verifica se a bola tocou a borda superior ou borda inferior do campo de jogos, caso positivo, muda a direção vertical da bola
        velocidade_bola_y *= -1

    # Colisão com barra esquerda
    #verifica se a bola atingiu a barra esquerda. Isso é feito comparando a coordenada horizontal da bola (x_bola) com a posição horizontal da barra esquerda (x_barra_esquerda) somada à sua largura (largura_barra). 
    if x_bola <= x_barra_esquerda + largura_barra: 
        velocidade_bola_x *= -1 #inverte a direção da bola

    # Colisão com barra direita
    #verifica se a bola atingiu a barra direita. Isso é feito comparando a coordenada horizontal da bola (x_bola) com a posição horizontal da barra direita (x_barra_direita) subtraída do tamanho da bola (tamanho_bola)
    if x_bola >= x_barra_direita - largura_barra: 
        velocidade_bola_x *= -1 #inverte a direção da bola

# Loop principal do jogo
executando = True
while executando:
    #a condição if evento.type == pygame.QUIT verifica se o evento corresponde ao usuário fechando a janela. 
    # Se for o caso, a variável executando é definida como False, fazendo com que o loop principal do jogo termine.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Movimentação das barras
    #Essa linha obtém o estado atual de todas as teclas do teclado e armazena em uma lista chamada teclas, se for presionada TRUE senão FALSE
    teclas = pygame.key.get_pressed()
    #verifica se as teclas foram pressionadas e não atingiram o final das telas e modificam o posuicionamento
    if teclas[pygame.K_w] and y_barra_esquerda > 0:
        y_barra_esquerda -= velocidade_barra
    if teclas[pygame.K_s] and y_barra_esquerda < ALTURA - altura_barra:
        y_barra_esquerda += velocidade_barra
    if teclas[pygame.K_UP] and y_barra_direita > 0:
        y_barra_direita -= velocidade_barra
    if teclas[pygame.K_DOWN] and y_barra_direita < ALTURA - altura_barra:
        y_barra_direita += velocidade_barra

    # Movimentação da bola
    mover_bola()

    # Desenho do jogo
    desenhar_jogo()

    # Controle de FPS
    clock.tick(FPS) #adiciona os 60 fps para o jogo

# Finaliza o pygame
pygame.quit()