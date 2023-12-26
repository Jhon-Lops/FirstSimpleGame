import pygame                  #biblioteca
from  pygame.locals import *   #submódulo, todas funções e constantes
from sys import exit           #para fechar a janela
from random import randint     #sorteia, aleatorio

pygame.init()                  #iniciar todas as funções e variáveis pygame

#Adicionando música
pygame.mixer.music.set_volume(0.1)                              #Volume da trilha
trilha = pygame.mixer.music.load("L'Esprit d'Sfign - X-plore.mp3")
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound("pickupCoin.wav")
barulho_colisao.set_volume(1)                                   #Volume dacolisão 0 =  desliga  1 = liga

#variaveis tela
largura = 640
altura = 480

#variaveis posição vermelho(avatar)
x = int(largura/2) - (40/2)
y = int(altura/2) - (50/2)

x_azul = randint(40, 600)                                  #inttervalo de numeros
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont("arial", 40, True, True)       #adc fonte - (fonte, tamanho, negrito, itálico)

tela = pygame.display.set_mode((largura, altura))          #criação da tela
pygame.display.set_caption("Jogo teste")
relogio = pygame.time.Clock()


#Loop
while True:                                               
    relogio.tick((30))

    tela.fill((0, 0, 0))

    mensagem = f"Pontos: {pontos}"                         #Mensagem de Pontos
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))       #(texto, cerrilhamento/pixelado, cor)
    
    for event in pygame.event.get():                       #função de fechar
        if event.type == QUIT:
            pygame.quit()
            exit()


        #Botões de comando
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''

        #Botões de comando pressionados
        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20


    #Ícone
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))         #retangulo, (cor=RGB), (x, y, largura, altura)
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))
                                                                               #pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40)    #circulo, (cor=RGB), (x, y) = meio do circulo =, raio
                                                                               #pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5) #linha, (cor=RGB), (x, y) inicio, (x, y) fim, expessura


    #Velocidade, opção
    ''''
    if y >= altura:
       y = 0 
    y = y + 5'''


    #Colisão
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)  
        y_azul = randint(50, 430)
        pontos = pontos + 1                                #Contagem de pontos
        barulho_colisao.play()
                                                
    tela.blit(texto_formatado, (430, 40))                  #Para texto aparecer na tela (texto, posição)
    pygame.display.update()


#Para verificar quais fontes estãoo disponiveis no nosso sistema, seguinte comando:
'''
pygame.font.get_fonts()'''