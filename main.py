import pygame
pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Iron Man")
branco = (255,255,255)
preto = (0,0,0)
posicaoXPersona = 275
posicaoYPersona = 236.5
movimentoXPersona = 0
movimentoYPersona = 0
fonte = pygame.font.SysFont("comicsans",14)
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load("assets/fundo.png")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 10
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPersona = -10
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPersona = 10
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPersona = -10
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPersona = 0

    posicaoXPersona = posicaoXPersona + movimentoXPersona   
    if posicaoXPersona < 0 :
        posicaoXPersona = 20
    elif posicaoXPersona > 550:
        posicaoXPersona = 540   

    posicaoYPersona = posicaoYPersona + movimentoYPersona 
    if posicaoYPersona < 0 :
        posicaoYPersona = 10
    elif posicaoYPersona > 473:
        posicaoYPersona = 463      

    tela.fill(branco)
    tela.blit(fundo, (0,0) )
    #pygame.draw.circle(tela, preto, (posicaoXPersona, posicaoYPersona), 40, 0)
    tela.blit( iron, (posicaoXPersona, posicaoYPersona) )
    texto = fonte.render(str(posicaoXPersona)+"-"+str(posicaoYPersona), True, branco)
    tela.blit(texto, (posicaoXPersona-30, posicaoYPersona-10))
              
    pygame.display.update()
    relogio.tick(60)
    