# Product class

class ButtonEvent:
    def __init__(self, button_x, button_y, button_width, button_height):
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height

    def get_button_x(self):
        return self.button_x

    def get_button_y(self):
        return self.button_y

    def get_button_width(self):
        return self.button_width

    def get_button_height(self):
        return self.button_height
