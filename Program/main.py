import pygame
from sys import exit
#Przydatne strony:
#https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=6357s (tutorial)
#https://coolors.co (gotowe palety barw, kreator palet)


pygame.init()
screen = pygame.display.set_mode((1000,720))

#roboczy uklad aplikacji (z wymiarami). Kolory przestrzeni w RGB
canvas = pygame.Surface((720,720))
canvas.fill(color=[130, 192, 204])
bookmarks = pygame.Surface((70,720))
bookmarks.fill(color=[237, 231, 227])
window = pygame.Surface((210,720))
window.fill(color=[255, 166, 43])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
#rozmieszczenie poszczegolnych przestrzeni roboczych
#kazda pozycja przestrzeni to lewy, gorny rog
    screen.blit(canvas,(280,0))
    screen.blit(bookmarks,(210,0))
    screen.blit(window,(0,0))

    pygame.display.update()