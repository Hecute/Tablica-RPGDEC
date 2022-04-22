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
-Menu
'''

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000,720))
bookmarks_buttons = pygame.sprite.Group()
menu_buttons_group = pygame.sprite.Group()
biome_buttons_group = pygame.sprite.Group()
map_elements = pygame.sprite.Group()

active_bookmark = 0 #Gdy klikniesz na zakładkę pierwszą to active_bookmark = 1 itp.
active_biome = 0

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
big_biome_pos = (canvas_pos + 80, 80)
medium_biome_pos = (canvas_pos + 320, 320)

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


#funkcja wywoływana w pętli
def display_window():
    # screen.blit(canvas, (canvas_pos, 0))
    #screen.blit(bookmarks, (245, 0))
    screen.blit(toolbox, (0, 0))

    bookmarks_buttons.update()
    bookmarks_buttons.draw(screen)
    #Gdy włączysz zakładkę "MENU" pojawiają się przyciski
    if active_bookmark == 1:
        biome_buttons_group.update()
        biome_buttons_group.draw(screen)
    elif active_bookmark == 5:
        menu_buttons_group.update()
        menu_buttons_group.draw(screen)
    pygame.display.update()


environment_button = BookmarkButtons((bookmark_x, 0), 'Biom', environment_color)
furniture_button = BookmarkButtons((bookmark_x, bookmark_height), 'Meble', furniture_color)
walls_button = BookmarkButtons((bookmark_x, bookmark_height*2), 'Ściany', walls_color)
misc_button = BookmarkButtons((bookmark_x, bookmark_height*3), 'Różne', misc_color)
menu_button = BookmarkButtons((bookmark_x, bookmark_height*4), 'Menu', menu_color)

#------TOOLBOX MENU BUTTONS-----


class MenuButtons(pygame.sprite.Sprite):
    def __init__(self, picture_path, position):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position





#------MENU BUTTONS-----
'''
zapis do pliku
przycisk do zmiany rozmiaru mapy
przycisk do obracania
przycisk do usuwania
'''
menu_save_button = MenuButtons("Pictures/Menu/menu_save_button.jpg", [122.5, 70])
menu_buttons_group.add(menu_save_button)
#------END MENU BUTTONS-----

#-----BIOME BUTTONS-----
class BiomeButtons(pygame.sprite.Sprite):
    def __init__(self, picture_path, position):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.full_image = self.image
        self.image = pygame.transform.scale(self.image, (75,75))
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw_terrain(self, position):
        screen.blit(self.full_image, position)


# biome_grass_big = BiomeButtons("Pictures/Biomes/grass_big.png", [70, 70])
# biome_buttons_group.add(biome_grass_big)
# biome_grass_medium = BiomeButtons("Pictures/Biomes/grass_medium.png", [175, 70])
# biome_buttons_group.add(biome_grass_medium)
#
# biome_cave_big = BiomeButtons("Pictures/Biomes/cave_big.png", [70, 170])
# biome_buttons_group.add(biome_cave_big)
# biome_cave_medium = BiomeButtons("Pictures/Biomes/cave_medium.png", [175, 170])
# biome_buttons_group.add(biome_cave_medium)
#
# biome_city_big = BiomeButtons("Pictures/Biomes/city_big.png", [70, 270])
# biome_buttons_group.add(biome_city_big)
# biome_city_medium = BiomeButtons("Pictures/Biomes/city_medium.png", [175, 270])
# biome_buttons_group.add(biome_city_medium)
#
# biome_water_big = BiomeButtons("Pictures/Biomes/water_big.png", [70, 370])
# biome_buttons_group.add(biome_water_big)
# biome_water_medium = BiomeButtons("Pictures/Biomes/water_medium.png", [175, 370])
# biome_buttons_group.add(biome_water_medium)
#
# biome_sand_big = BiomeButtons("Pictures/Biomes/sand_big.png", [70, 470])
# biome_buttons_group.add(biome_sand_big)
# biome_sand_medium = BiomeButtons("Pictures/Biomes/sand_medium.png", [175, 470])
# biome_buttons_group.add(biome_sand_medium)


#-----END BIOME BUTTONS-----

screen.blit(canvas, (canvas_pos, 0))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #sprawdzanie zakładek
            if environment_button.rect.collidepoint(pygame.mouse.get_pos()):
                active_bookmark = 1
                toolbox.fill(color=environment_color)
            elif furniture_button.rect.collidepoint(pygame.mouse.get_pos()):
                active_bookmark = 2
                toolbox.fill(color=furniture_color)
            elif walls_button.rect.collidepoint(pygame.mouse.get_pos()):
                active_bookmark = 3
                toolbox.fill(color=walls_color)
            elif misc_button.rect.collidepoint(pygame.mouse.get_pos()):
                active_bookmark = 4
                toolbox.fill(color=misc_color)
            elif menu_button.rect.collidepoint(pygame.mouse.get_pos()):
                active_bookmark = 5
                toolbox.fill(color=menu_color)
            #sprawdzanie przycisków w zakładkach
            elif active_bookmark == 1:
                # if biome_grass_big.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_grass_big.draw_terrain(big_biome_pos)
                # elif biome_grass_medium.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_grass_medium.draw_terrain(medium_biome_pos)
                #
                # elif biome_cave_big.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_cave_big.draw_terrain(big_biome_pos)
                # elif biome_cave_medium.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_cave_medium.draw_terrain(medium_biome_pos)
                #
                # elif biome_city_big.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_city_big.draw_terrain(big_biome_pos)
                # elif biome_city_medium.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_city_medium.draw_terrain(medium_biome_pos)
                #
                # elif biome_water_big.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_water_big.draw_terrain(big_biome_pos)
                # elif biome_water_medium.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_water_medium.draw_terrain(medium_biome_pos)
                #
                # elif biome_sand_big.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_sand_big.draw_terrain(big_biome_pos)
                # elif biome_sand_medium.rect.collidepoint(pygame.mouse.get_pos()):
                #     screen.blit(canvas, (canvas_pos, 0))
                #     biome_sand_medium.draw_terrain(medium_biome_pos)


                map_elements.update()
                map_elements.draw(screen)
            elif active_bookmark == 5 and menu_save_button.rect.collidepoint(pygame.mouse.get_pos()):
                print("saved")

    # rozmieszczenie poszczegolnych przestrzeni roboczych
    # kazda pozycja przestrzeni to lewy, gorny rog
    display_window()
    # if active_bookmark == 1:
    #     if biom_grass_big.rect.collidepoint(pygame.mouse.get_pos()):
    #         # biom_grass_big.draw_terrain((canvas_pos,80))
    #         screen.blit(biom_grass_big.image, (canvas_pos + 80, 80))
