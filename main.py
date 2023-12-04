# Deadline - 15th of December 2023
# Mail with:
# 1. short screen recording demonstrating the new features
# 2. Linked code

import pygame
import numpy as np

from Data import data
from ButtonEventBuilderPattern.ButtonEventSetUp import EventSetUpClass
from ButtonsFactoryPattern.ButtonFactoryClass import StopButtonFactory, SaveButtonFactory, StartButtonFactory, \
    LoadButtonFactory

# Initialize Pygame
pygame.init()

# Game state
game_state = np.random.choice([0, 1], size=(data.n_cells_x, data.n_cells_y), p=[0.8, 0.2])


# Factory Pattern ===========================================
def draw_buttons():
    StartButtonFactory().CreateButton().draw_button()
    StopButtonFactory().CreateButton().draw_button()
    SaveButtonFactory().CreateButton().draw_button()
    LoadButtonFactory().CreateButton().draw_button()


# ==========================================================

def draw_cells():
    for y in range(data.n_cells_y):
        for x in range(data.n_cells_x):
            cell = pygame.Rect(x * data.cell_width, y * data.cell_height, data.cell_width, data.cell_height)
            if game_state[x, y] == 1:
                pygame.draw.rect(data.screen, data.black, cell)


def draw_grid():
    for y in range(0, data.height, data.cell_height):
        for x in range(0, data.width, data.cell_width):
            cell = pygame.Rect(x, y, data.cell_width, data.cell_height)
            pygame.draw.rect(data.screen, data.gray, cell, 1)


def update_grid():
    global game_state
    new_state = np.copy(game_state)
    for y in range(data.n_cells_y):
        for x in range(data.n_cells_x):
            n_neighbors = game_state[(x - 1) % data.n_cells_x, (y - 1) % data.n_cells_y] + \
                          game_state[x % data.n_cells_x, (y - 1) % data.n_cells_y] + \
                          game_state[(x + 1) % data.n_cells_x, (y - 1) % data.n_cells_y] + \
                          game_state[(x - 1) % data.n_cells_x, y % data.n_cells_y] + \
                          game_state[(x + 1) % data.n_cells_x, y % data.n_cells_y] + \
                          game_state[(x - 1) % data.n_cells_x, (y + 1) % data.n_cells_y] + \
                          game_state[x % data.n_cells_x, (y + 1) % data.n_cells_y] + \
                          game_state[(x + 1) % data.n_cells_x, (y + 1) % data.n_cells_y]

            if game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                new_state[x, y] = 0
            elif game_state[x, y] == 0 and n_neighbors == 3:
                new_state[x, y] = 1

    game_state = new_state


def fill_data():
    data.screen.fill(data.white)
    draw_grid()
    draw_cells()
    draw_buttons()
    pygame.display.flip()


def main():
    running = True
    while running:

        # Data Every think that need to be done to build up project
        fill_data()

        # =========================================================

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Builder Pattern ================================
                EventSetUpClass(event, game_state).EventListener()
                # ================================================

        # Real time ====================
        if data.running_simulation:
            update_grid()

        pygame.time.delay(data.interval)
        data.timer.tick(60)
        # ==============================
    pygame.quit()


if __name__ == "__main__":
    main()
