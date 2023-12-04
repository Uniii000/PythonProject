from Interfaces.ButtonDrawInterface import IButtonDrawInterface
import pygame
from Data import data


class LoadButton(IButtonDrawInterface):

    def draw_button(self, **kwargs):
        pygame.draw.rect(data.screen, data.gray,
                         (data.load_button_x, data.load_button_y,
                          data.button_width, data.button_height))
        font = pygame.font.Font(None, 36)
        text = font.render("Load", True, data.white)
        text_rect = text.get_rect(center=(data.load_button_x + data.button_width // 2,
                                          data.load_button_y + data.button_height // 2))
        data.screen.blit(text, text_rect)

