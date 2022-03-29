import pygame
from sys import exit
#Przydatne strony:
#https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=6357s (tutorial)
#https://coolors.co (gotowe palety barw, kreator palet)

'''
-środowisko
-meble
-ściany
-obiekty
-menu
'''

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000,720))
bookmarks_buttons = pygame.sprite.Group()

#kolory
canvas_color = [130, 192, 204]
bookmarks_color = [237, 231, 227]
toolbox_color = [255, 166, 43]

environment_color = [194, 226, 101]
furniture_color = [190, 141, 96]
walls_color = [150, 144, 115]
misc_color = [117, 158, 184]
menu_color = [189, 197, 199]


#roboczy uklad aplikacji (z wymiarami). Kolory przestrzeni w RGB
canvas = pygame.Surface((720, 720))
canvas.fill(color=canvas_color)
bookmarks = pygame.Surface((35, 720))
bookmarks.fill(color=bookmarks_color)
toolbox = pygame.Surface((245, 720))
toolbox.fill(color=toolbox_color)
canvas_pos = toolbox.get_width() + bookmarks.get_width()

# Wymiary i położenie przycisków paska zakładek
bookmarks_number = 5
bookmark_width = bookmarks.get_width()
bookmark_height = bookmarks.get_height()/bookmarks_number
bookmark_x = toolbox.get_width()

class BookmarkButtons(pygame.sprite.Sprite):
    def __init__(self, position, text, colors):
        super().__init__()
        self.colors = colors
        self.font = pygame.font.SysFont("Arial", 30)
        self.text_render = self.font.render(text, True, (0, 0, 0))
        self.text_render = pygame.transform.rotate(self.text_render, 270)
        # zamienić Surface na image.load
        self.image = pygame.Surface([bookmark_width,bookmark_height])
        self.image.fill(self.colors)
        self.x, self.y = position
        self.width = bookmark_width
        self.height = bookmark_height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.update()
        bookmarks_buttons.add(self)

    def update(self):
        pygame.draw.rect(screen, self.colors, (self.x, self.y, self.width, self.height))


def display_window():
    screen.blit(canvas, (canvas_pos, 0))
    #screen.blit(bookmarks, (245, 0))
    screen.blit(toolbox, (0, 0))

    bookmarks_buttons.update()
    bookmarks_buttons.draw(screen)

    pygame.display.update()


environment_button = BookmarkButtons((bookmark_x, 0), 'Biom', environment_color)
furniture_button = BookmarkButtons((bookmark_x, bookmark_height), 'Meble', furniture_color)
walls_button = BookmarkButtons((bookmark_x, bookmark_height*2), 'Ściany', walls_color)
misc_button = BookmarkButtons((bookmark_x, bookmark_height*3), 'Różne', misc_color)
menu_button = BookmarkButtons((bookmark_x, bookmark_height*4), 'Menu', menu_color)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if environment_button.rect.collidepoint(pygame.mouse.get_pos()):
                toolbox.fill(color=environment_color)
            elif furniture_button.rect.collidepoint(pygame.mouse.get_pos()):
                toolbox.fill(color=furniture_color)
            elif walls_button.rect.collidepoint(pygame.mouse.get_pos()):
                toolbox.fill(color=walls_color)
            elif misc_button.rect.collidepoint(pygame.mouse.get_pos()):
                toolbox.fill(color=misc_color)
            elif menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                toolbox.fill(color=menu_color)

    # rozmieszczenie poszczegolnych przestrzeni roboczych
    # kazda pozycja przestrzeni to lewy, gorny rog
    display_window()