import pygame

pygame.init()
screen = pygame.display.set_mode((1550, 800))
pygame.display.set_caption("歴戦乱舞")

sample_image = pygame.image.load("img/超武闘派アサシン.png")

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(sample_image, ((1550-1024) / 2, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
