from Interfaces.ButtonEventInterface import IButtonEvent
from ButtonEventBuilderPattern.ButtonEvent import ButtonEvent


# Builder class
class Builder(IButtonEvent):

    def __init__(self):
        self.buttonBuilder = ButtonEvent(button_x=0, button_y=0, button_width=0, button_height=0)

    def set_button_x(self, button_x):
        self.buttonBuilder.button_x = button_x
        return self

    def set_button_y(self, button_y):
        self.buttonBuilder.button_y = button_y
        return self

    def set_button_width(self, button_width):
        self.buttonBuilder.button_width = button_width
        return self

    def set_button_height(self, button_height):
        self.buttonBuilder.button_height = button_height
        return self

    def get_button_x(self):
        return self.buttonBuilder.get_button_x()

    def get_button_y(self):
        return self.buttonBuilder.get_button_y()

    def get_button_width(self):
        return self.buttonBuilder.get_button_width()

    def get_button_height(self):
        return self.buttonBuilder.get_button_height()

    def get_result(self):  # Add the build method
        return self.buttonBuilder
