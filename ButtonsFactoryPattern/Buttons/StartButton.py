from Interfaces.ButtonDrawInterface import IButtonDrawInterface
import pygame
from Data import data


class StartButton(IButtonDrawInterface):

    def draw_button(self, **kwargs):
        pygame.draw.rect(data.screen, data.gray,
                         (data.start_button_x, data.start_button_y, data.button_width, data.button_height))
        font = pygame.font.Font(None, 36)
        text = font.render("Start", True, data.white)
        text_rect = text.get_rect(
            center=(data.start_button_x + data.button_width // 2, data.start_button_y + data.button_height // 2))
        data.screen.blit(text, text_rect)

