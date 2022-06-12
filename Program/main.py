import pygame
from sys import exit
from os.path import exists
import tkinter as tk
from tkinter import filedialog
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
furniture_buttons_group = pygame.sprite.Group()
terrain = pygame.sprite.Group()
grid = pygame.sprite.Group()
map_elements = pygame.sprite.Group()

active_bookmark = 0 #Gdy klikniesz na zakładkę pierwszą to active_bookmark = 1 itp.
active_biome = 0
tool_selected = 0

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
# toolbox.fill(color=toolbox_color)
toolbox = pygame.image.load("Pictures/ToolBoxes/Default_ToolBox.png")
canvas_pos = toolbox.get_width() + bookmarks.get_width()
canvas_center = (640, 360)
big_biome_pos = (canvas_pos + 80, 80)
medium_biome_pos = (canvas_pos + 320, 320)

# Wymiary i położenie przycisków paska zakładek
bookmarks_number = 5
bookmark_width = bookmarks.get_width()
bookmark_height = bookmarks.get_height()/bookmarks_number
bookmark_x = toolbox.get_width()

class BookmarkButtons(pygame.sprite.Sprite):
    def __init__(self, position, text, image_path):
        super().__init__()
        # self.colors = colors
        # self.font = pygame.font.SysFont("Arial", 30)
        self.font = pygame.font.Font("Font/BPdotsUnicaseSquareBold.otf",30)
        self.textSurf = self.font.render(text, 1, "WHITE")
        self.textSurf = pygame.transform.rotate(self.textSurf,270)
        # self.image = pygame.Surface([bookmark_width,bookmark_height])
        # self.image.fill(self.colors)
        # self.image = pygame.image.load("Pictures/Bookmarks/Biome_BookMark.png")
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.x, self.y = position
        self.width = bookmark_width
        self.height = bookmark_height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image.blit(self.textSurf,[bookmark_width/2 - self.width/2, bookmark_height/2 - self.height/2 + 10])
        self.update()
        bookmarks_buttons.add(self)

    # def update(self):
        # pygame.draw.rect(screen, self.colors, (self.x, self.y, self.width, self.height))





environment_button = BookmarkButtons((bookmark_x, 0), 'Biom', "Pictures/Bookmarks/Biome_BookMark.png")
furniture_button = BookmarkButtons((bookmark_x, bookmark_height), 'Meble', "Pictures/Bookmarks/Furniture_BookMark.png")
walls_button = BookmarkButtons((bookmark_x, bookmark_height*2), 'Ściany', "Pictures/Bookmarks/Walls_BookMark.png")
misc_button = BookmarkButtons((bookmark_x, bookmark_height*3), 'Różne', "Pictures/Bookmarks/Others_BookMark.png")
menu_button = BookmarkButtons((bookmark_x, bookmark_height*4), 'Menu', "Pictures/Bookmarks/Menu_BookMark.png")

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
czyszczenie mapy
'''
menu_save_button = MenuButtons("Pictures/Menu/menu_save_button.png", [122.5, 90])
menu_buttons_group.add(menu_save_button)

menu_delete_button = MenuButtons("Pictures/Menu/menu_delete_button.png", [122.5, 180])
menu_buttons_group.add(menu_delete_button)

menu_eraser = MenuButtons("Pictures/Menu/menu_eraser_button.png", [122.5, 270])
menu_buttons_group.add(menu_eraser)

menu_square_grid = MenuButtons("Pictures/Menu/menu_square_grid.png", [122.5, 360])
menu_square_grid.image = pygame.transform.scale(menu_square_grid.image, (80,80))
menu_buttons_group.add(menu_square_grid)

menu_hex_grid = MenuButtons("Pictures/Menu/menu_hex_grid.png", [122.5, 450])
menu_hex_grid.image = pygame.transform.scale(menu_hex_grid.image, (80,80))
menu_buttons_group.add(menu_hex_grid)

menu_no_grid = MenuButtons("Pictures/Menu/menu_no_grid.png", [122.5, 540])
menu_no_grid.image = pygame.transform.scale(menu_no_grid.image, (80,80))
menu_buttons_group.add(menu_no_grid)




#------END MENU BUTTONS-----

#-----BIOME BUTTONS-----
class BiomeButtons(pygame.sprite.Sprite):
    def __init__(self, picture_path, position):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (75,75))
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position



biome_grass_big = BiomeButtons("Pictures/Biomes/grass_big.png", [70, 160])
biome_buttons_group.add(biome_grass_big)
biome_grass_medium = BiomeButtons("Pictures/Biomes/grass_medium.png", [175, 160])
biome_buttons_group.add(biome_grass_medium)

biome_cave_big = BiomeButtons("Pictures/Biomes/cave_big.png", [70, 260])
biome_buttons_group.add(biome_cave_big)
biome_cave_medium = BiomeButtons("Pictures/Biomes/cave_medium.png", [175, 260])
biome_buttons_group.add(biome_cave_medium)

biome_city_big = BiomeButtons("Pictures/Biomes/city_big.png", [70, 360])
biome_buttons_group.add(biome_city_big)
biome_city_medium = BiomeButtons("Pictures/Biomes/city_medium.png", [175, 360])
biome_buttons_group.add(biome_city_medium)

biome_water_big = BiomeButtons("Pictures/Biomes/water_big.png", [70, 460])
biome_buttons_group.add(biome_water_big)
biome_water_medium = BiomeButtons("Pictures/Biomes/water_medium.png", [175, 460])
biome_buttons_group.add(biome_water_medium)

biome_sand_big = BiomeButtons("Pictures/Biomes/sand_big.png", [70, 560])
biome_buttons_group.add(biome_sand_big)
biome_sand_medium = BiomeButtons("Pictures/Biomes/sand_medium.png", [175, 560])
biome_buttons_group.add(biome_sand_medium)


#-----END BIOME BUTTONS-----

#-----MAP ELEMENTS-----
class MapElement(pygame.sprite.Sprite):
    def __init__(self, picture_path, position):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.cursor = picture_path
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw_element(self, position):
        screen.blit(self.image, position)

#-----FURNITURE BUTTONS-----
chair = MapElement("Pictures/Furniture/chair.png", [45, 60])
furniture_buttons_group.add(chair)

table_small = MapElement("Pictures/Furniture/table_small.png", [95, 60])
furniture_buttons_group.add(table_small)

table_long = MapElement("Pictures/Furniture/table_long1.png", [170, 60])
furniture_buttons_group.add(table_long)

barrel = MapElement("Pictures/Furniture/barrel.png", [50, 110])
furniture_buttons_group.add(barrel)

bed_small = MapElement("Pictures/Furniture/bed_small1.png", [100, 130])
furniture_buttons_group.add(bed_small)

bed_big = MapElement("Pictures/Furniture/bed_big.png", [175, 130])
furniture_buttons_group.add(bed_big)

wardrobe_small = MapElement("Pictures/Furniture/wardrobe_small.png", [50, 180])
furniture_buttons_group.add(wardrobe_small)

bench_long = MapElement("Pictures/Furniture/bench_long.png", [120, 185])
furniture_buttons_group.add(bench_long)



rotate_left = MapElement("Pictures/Furniture/barrel.png", [65, 600])
furniture_buttons_group.add(rotate_left)

rotate_right = MapElement("Pictures/Furniture/barrel.png", [100, 600])
furniture_buttons_group.add(rotate_right)

brush = 0

def rotate_sprite_left():
    if tool_selected == 1:
        brush_name = brush.cursor
        brush_rotate = brush_name[-5::5]
        if brush_rotate == '1' or brush_rotate == '2' or \
                brush_rotate == '3' or brush_rotate == '4':
            brush_rotate = int(brush_rotate)
            if brush_rotate == 4:
                brush_rotate = 1
            else:
                brush_rotate += 1
            brush_temp = brush_name[:-5] + str(brush_rotate) + brush_name[-4::1]
            brush_name = brush_temp

            if exists(brush_name):
                brush.cursor = brush_name
            else:
                brush_temp = brush_name[:-5] + '1' + brush_name[-4::1]
                brush_name = brush_temp
                brush.cursor = brush_name


def rotate_sprite_right():
    if tool_selected == 1:
        brush_name = brush.cursor
        brush_rotate = brush_name[-5::5]
        if brush_rotate == '1' or brush_rotate == '2' or \
                brush_rotate == '3' or brush_rotate == '4':
            brush_rotate = int(brush_rotate)
            if brush_rotate == 1:
                brush_rotate = 4
            else:
                brush_rotate -= 1
            brush_temp = brush_name[:-5] + str(brush_rotate) + brush_name[-4::1]
            brush_name = brush_temp

            if exists(brush_name):
                brush.cursor = brush_name
            else:
                brush_temp = brush_name[:-5] + '2' + brush_name[-4::1]
                brush_name = brush_temp
                brush.cursor = brush_name


#funkcja wywoływana w pętli
def display_window():
    screen.blit(canvas, (canvas_pos, 0))
    #screen.blit(bookmarks, (245, 0))
    screen.blit(toolbox, (0, 0))

    bookmarks_buttons.update()
    bookmarks_buttons.draw(screen)
    #Gdy włączysz zakładkę "MENU" pojawiają się przyciski
    if active_bookmark == 1:
        biome_buttons_group.update()
        biome_buttons_group.draw(screen)
    elif active_bookmark == 2:
        furniture_buttons_group.update()
        furniture_buttons_group.draw(screen)
    elif active_bookmark == 5:
        menu_buttons_group.update()
        menu_buttons_group.draw(screen)

    terrain.update()
    terrain.draw(screen)
    map_elements.update()
    map_elements.draw(screen)
    grid.update()
    grid.draw(screen)

    if pygame.mouse.get_pos() >= (canvas_pos, 0) and pygame.mouse.get_pos() <= (1000, 720) and tool_selected !=0:
        pygame.mouse.set_visible(False)
        cords = pygame.mouse.get_pos()
        cursor_rect = cursor.get_rect()
        cursor_rect.center = cords
        screen.blit(cursor, cursor_rect)
    else:
        pygame.mouse.set_visible(True)
    pygame.display.update()





screen.blit(canvas, (canvas_pos, 0))
cursor = pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_cords = pygame.mouse.get_pos()
            if environment_button.rect.collidepoint(mouse_cords):
                active_bookmark = 1
                cursor = pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                tool_selected = 0
                toolbox = pygame.image.load("Pictures/ToolBoxes/Biome_ToolBox.png")
            elif furniture_button.rect.collidepoint(mouse_cords):
                active_bookmark = 2
                cursor = pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                tool_selected = 0
                toolbox = pygame.image.load("Pictures/ToolBoxes/Furniture_ToolBox.png")
            elif walls_button.rect.collidepoint(mouse_cords):
                active_bookmark = 3
                cursor = pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                tool_selected = 0
                toolbox = pygame.image.load("Pictures/ToolBoxes/Walls_ToolBox.png")
            elif misc_button.rect.collidepoint(mouse_cords):
                active_bookmark = 4
                cursor = pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                tool_selected = 0
                toolbox = pygame.image.load("Pictures/ToolBoxes/Others_ToolBox.png")
            elif menu_button.rect.collidepoint(mouse_cords):
                active_bookmark = 5
                cursor = pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                tool_selected = 0
                toolbox = pygame.image.load("Pictures/ToolBoxes/Menu_ToolBox.png")
            #sprawdzanie przycisków w zakładkach
            elif active_bookmark == 1:
                if biome_grass_big.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/grass_big.png", canvas_center))
                elif biome_grass_medium.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/grass_medium.png", canvas_center))
                elif biome_cave_big.rect.collidepoint(mouse_cords):
                  terrain.empty()
                  terrain.add(MapElement("Pictures/Biomes/cave_big.png", canvas_center))
                elif biome_cave_medium.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/cave_medium.png", canvas_center))

                elif biome_city_big.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/city_big.png", canvas_center))
                elif biome_city_medium.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/city_medium.png", canvas_center))

                elif biome_water_big.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/water_big.png", canvas_center))
                elif biome_water_medium.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/water_medium.png", canvas_center))

                elif biome_sand_big.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/sand_big.png", canvas_center))
                elif biome_sand_medium.rect.collidepoint(mouse_cords):
                    terrain.empty()
                    terrain.add(MapElement("Pictures/Biomes/sand_medium.png", canvas_center))

            elif active_bookmark == 2:
                if chair.rect.collidepoint(mouse_cords):
                    brush = chair
                    tool_selected = 1
                elif table_small.rect.collidepoint(mouse_cords):
                    brush = table_small
                    tool_selected = 1
                elif table_long.rect.collidepoint(mouse_cords):
                    brush = table_long
                    tool_selected = 1
                elif barrel.rect.collidepoint(mouse_cords):
                    brush = barrel
                    tool_selected = 1
                elif bed_small.rect.collidepoint(mouse_cords):
                    brush = bed_small
                    tool_selected = 1
                elif bed_big.rect.collidepoint(mouse_cords):
                    brush = bed_big
                    tool_selected = 1
                elif wardrobe_small.rect.collidepoint(mouse_cords):
                    brush = wardrobe_small
                    tool_selected = 1
                elif bench_long.rect.collidepoint(mouse_cords):
                    brush = bench_long
                    tool_selected = 1

                elif rotate_left.rect.collidepoint(mouse_cords):
                    rotate_sprite_left()
                elif rotate_right.rect.collidepoint(mouse_cords):
                    rotate_sprite_right()

                elif mouse_cords >= (canvas_pos, 0) and mouse_cords <= (1000, 720) and tool_selected == 1:
                    map_elements.add(MapElement(brush.cursor, mouse_cords))

                if tool_selected == 1:
                    cursor = pygame.image.load(brush.cursor).convert_alpha()

            elif active_bookmark == 5:
                if menu_save_button.rect.collidepoint(mouse_cords):
                    root = tk.Tk()
                    root.withdraw()
                    path = filedialog.asksaveasfilename(initialdir="/",
                                                        title="Select file",
                                                        filetypes=(("png files", "*.png"), ("All", "*.*")),
                                                        defaultextension=".png")
                    if path:
                        print(path)
                        rect = pygame.Rect(280, 0, 720, 720)
                        screenshot = screen.subsurface(rect)
                        pygame.image.save(screenshot, path)

                elif menu_delete_button.rect.collidepoint(mouse_cords):
                    map_elements.empty()
                    terrain.empty()
                    grid.empty()

                elif menu_eraser.rect.collidepoint(mouse_cords):
                    tool_selected = 2
                    cursor = pygame.image.load("Pictures/Menu/eraser2.png").convert_alpha()
                    # cursor = pygame.transform.scale(cursor, (50, 50))

                elif menu_square_grid.rect.collidepoint(mouse_cords):
                    grid.empty()
                    grid.add(MapElement("Pictures/Menu/square_grid.png", canvas_center))
                elif menu_hex_grid.rect.collidepoint(mouse_cords):
                    grid.empty()
                    grid.add(MapElement("Pictures/Menu/hex_grid_thin.png", canvas_center))
                elif menu_no_grid.rect.collidepoint(mouse_cords):
                    grid.empty()

                elif mouse_cords >= (canvas_pos, 0) and mouse_cords <= (1000, 720) and tool_selected == 2:
                    sprites = map_elements.sprites()
                    for item in sprites[::-1]:
                        if item.rect.collidepoint(mouse_cords):
                            item.kill()
                            break

        if event.type == pygame.KEYDOWN:
            if tool_selected == 1:
                if event.key == pygame.K_q:
                    rotate_sprite_left()
                elif event.key == pygame.K_e:
                    rotate_sprite_right()
                elif event.key == pygame.K_ESCAPE:
                    tool_selected = 0

                cursor = pygame.image.load(brush.cursor).convert_alpha()

            if event.key == pygame.K_g:
                    grid.empty()
                    grid.add(MapElement("Pictures/Menu/square_grid.png", canvas_center))
            elif event.key == pygame.K_h:
                    grid.empty()
                    grid.add(MapElement("Pictures/Menu/hex_grid_thin.png", canvas_center))
            elif event.key == pygame.K_n:
                    grid.empty()








    # rozmieszczenie poszczegolnych przestrzeni roboczych
    # kazda pozycja przestrzeni to lewy, gorny rog
    display_window()