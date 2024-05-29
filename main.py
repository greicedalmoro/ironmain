import pygame
pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Iron Man do Marcão")
branco = (255,255,255)
preto = (0,0,0)
posicaoXPersona = 400
posicaoYPersona = 300
movimentoPersona = 0
fonte = pygame.font.SysFont("comicsans",14)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoPersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoPersona = -5
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoPersona = 0

    posicaoXPersona = posicaoXPersona + movimentoPersona            
    if posicaoXPersona < 0 :
        posicaoXPersona = 10
    elif posicaoXPersona > 800:
        posicaoXPersona = 790    
        
    tela.fill(branco)
    pygame.draw.circle(tela, preto, (posicaoXPersona, posicaoYPersona), 40, 0)
    texto = fonte.render(str(posicaoXPersona)+"-"+str(posicaoYPersona), True, branco)
    tela.blit(texto, (posicaoXPersona-30, posicaoYPersona-10))
              
    pygame.display.update()
    relogio.tick(60)
    