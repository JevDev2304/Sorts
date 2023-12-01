import pygame
import random
pygame.init()
class DrawInformation:
    RED = 255,0,0
    GREEN = 0, 255,0
    BLUE = 0,0, 255
    BLACK =0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255, 0, 0
    GREY = 90,90,90
    LAVANDA = 230, 230, 250
    MELOCOTON  = 255, 218, 185
    MENTA =152,255,178
    BACKGROUND_COLOR = WHITE
    SIDE_PAD = 100
    TOP_PAD = 150

    GRADIENTS = [
        RED,
        GREEN,
        BLUE
    ]
    FONT = pygame.font.SysFont("candara",18)
    LARGE_FONT =pygame.font.SysFont("candara",25)

    def __init__(self,width,height,lst):
        self.width= width
        self.height  = height
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)
    def set_list(self,lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)
        self.block_width = round((self.width -self.SIDE_PAD) /len(lst))
        self.block_height =(self.height-self.TOP_PAD)/ (self.max_val-self.min_val)
        self.start_x = self.SIDE_PAD //2


def generate_starting_list(n,min_val,max_val):
    lst = [random.randint(min_val,max_val) for _ in range (n)]
    return lst
def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    controls = draw_info.FONT.render("R - Reiniciar | ESPACIO - Iniciar ordenamiento | A - De forma ascendente | D - De forma descendente",1,draw_info.BLACK)
    draw_info.window.blit(controls,(draw_info.width /2 -controls.get_width()/2,5))
    sorting = draw_info.FONT.render(
        "I - Inserción | B - Burbuja | M - Mezcla| P - Rapido | X - Radix | C - Cuentas | S - Casilleros ", 1,
        draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width / 2 - controls.get_width() / 2, 35))

    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg = False):
    lst = draw_info.lst
    if clear_bg:
        clear_rect =(draw_info.SIDE_PAD//2,draw_info.TOP_PAD,
                     draw_info.width-draw_info.SIDE_PAD,draw_info.height-draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window,draw_info.BACKGROUND_COLOR, clear_rect)
        pygame.draw.rect()
    for i, val in enumerate(lst):
        x= draw_info.start_x +i * draw_info.block_width
        y = draw_info.height -(val-draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color,(x,y,draw_info.block_width,draw_info.height), border_radius=20)
    if clear_bg:
        pygame.display.update()

def bubble_sort(draw_info,ascending = True):
    lst = draw_info.lst
    for i in range(len(lst)-1):
        for j in range (len(lst)-1-i):
            num1 = lst[i]
            num2 = lst[j]
            if num1> num2 and ascending:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info,{j:draw_info.BLACK,j+1:draw_info.GREY})
                yield True
    return lst



