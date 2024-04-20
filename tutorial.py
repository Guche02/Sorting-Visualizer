import pygame
import math
from algorithms import generate_starting_list,bubble_sort, insertion_sort, selection_sort
pygame.init()   # to  initialize pygame

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    RED = 255, 0, 0 
    GREEN = 0, 255, 0
    BLUE = 0, 0, 255
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    GRADIENTS = [ (0,128,191), (0,172,223), (85,208,255) ]

    FONT = pygame.font.SysFont('comicsans', 15)       # setting the font for display
    LARGE_FONT = pygame.font.SysFont('comicsans', 20)

    SIDE_PAD = 100         # padding of 60 pixels on the right side, 50 pixels on the left side.
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithm Visualization')
        self.set_list(lst)   # it is invoked everytime a object is created

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)   

        self.block_width = round((self.width - self.SIDE_PAD)/len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD)/(self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.FONT.render(f"{algo_name} -{'Ascending' if ascending else 'Descending'}", 1, draw_info.RED)  
    draw_info.window.blit(title, ( draw_info.width/2 - title.get_width()/2, 5))   
    
    controls = draw_info.FONT.render("R - RESET || SPACE - Start Sorting || A - Ascending || D - Descending", 1, draw_info.BLACK)  # for rendering the text
    draw_info.window.blit(controls, ( draw_info.width/2 - controls.get_width()/2, 25))   # controls.get_width() is used to get the width of the text above.
    # to center the text at the window.
    # blit is used to draw one surface on the top of another
    # In this case, controls is being drawn on top of the window

    sorting = draw_info.FONT.render("B - Bubble Sort || I - Insertion Sort || S - Selection Sort ",1, draw_info.BLACK)  # for rendering the text, 1 is used for anti-aliasing effect (less pixelated)
    draw_info.window.blit(sorting, ( draw_info.width/2 - sorting.get_width()/2, 45))   # controls.get_width() is used to get the width of the text above.

 
    draw_list(draw_info)     
    pygame.display.update()  # updates the window screen

def draw_list(draw_info, color_positions = {}, clear_bg = False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)  #(x,y,width, height) 
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):   #gives index and value
        X = draw_info.start_x + i * draw_info.block_width

        Y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height
        # the pixel values start from the top left, so we need to subtract the values from the height.
        # subtacting the val from min_val as to find the range with respect to the min_value, so that the block height is not ridiculously high.
        
        color = draw_info.GRADIENTS[i % 3]   #0,1,2 (different gradients color)

        if i in color_positions:
            color = color_positions[i]


        pygame.draw.rect(draw_info.window, color, (X,Y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()    # decides the delay to show the changes made

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True

    sorting_algorithm = None
    algo_name = None
    sorting_algorithm_generator = None

    while run:
        clock.tick(10)  # the higher the faster.

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:   # once the generator is finished, stopIteration is handled
                sorting = False
        else:
            draw(draw_info, draw_list ,algo_name, ascending)

        for event in pygame.event.get(): # gets every event that has been occuring in the running loop (running window)
            if event.type == pygame.QUIT:   # hitting the red cross button on the window screen
                run = False

            if event.type != pygame.KEYDOWN:  # no key is pressed
                continue

            if event.key == pygame.K_r:   # r is pressed
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False

            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending) 
            
            elif event.key == pygame.K_a and sorting== False:
                ascending = True
            
            elif event.key == pygame.K_d and sorting == False:
                ascending = False

            elif event.key == pygame.K_i and sorting == False:
                sorting_algorithm = insertion_sort
                algo_name = "Insertion Sort"

            elif event.key == pygame.K_b and sorting == False:
                sorting_algorithm = bubble_sort
                algo_name = "Bubble Sort"

            elif event.key == pygame.K_s and sorting == False:
                sorting_algorithm = selection_sort
                algo_name = "Selection Sort"
                
    pygame.quit()

if __name__ == '__main__':   # setting the top-level code (entry point code) to main(), useful when the script is imported as modules in other programs.
    main()


        

        
