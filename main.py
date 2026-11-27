import pygame
pygame.init()
screen = pygame.display.set_mode((800, 450))
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    screen.fill((200, 110, 10))
    pygame.display.flip()
pygame.quit()