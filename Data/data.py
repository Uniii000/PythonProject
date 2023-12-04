import pygame

# Created for data storage

# Screen dimensions
width, height = 900, 600
screen = pygame.display.set_mode((width, height))

# Grid dimensions
n_cells_x, n_cells_y = 50, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (0, 255, 0)

# Button dimensions
button_width, button_height = 200, 50

# Button x,y for every case
start_button_x, start_button_y = 20,0
stop_button_x, stop_button_y = 240,0
save_button_x, save_button_y = 460,0
load_button_x, load_button_y = 680,0

# Real-time variables
interval = 100
timer = pygame.time.Clock()

# Variable
running_simulation = False
