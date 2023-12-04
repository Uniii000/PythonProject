from abc import ABC, abstractmethod


# Builder Interface
class IButtonEvent(ABC):
    @staticmethod
    @abstractmethod
    def set_button_x(button_x):
        pass

    @staticmethod
    @abstractmethod
    def set_button_y(button_y):
        pass

    @staticmethod
    @abstractmethod
    def set_button_width(button_width):
        pass

    @staticmethod
    @abstractmethod
    def set_button_height(button_height):
        pass

    @staticmethod
    @abstractmethod
    def get_button_x(button_x):
        pass

    @staticmethod
    @abstractmethod
    def get_button_y(button_y):
        pass

    @staticmethod
    @abstractmethod
    def get_button_width(button_width):
        pass

    @staticmethod
    @abstractmethod
    def get_button_height(button_height):
        pass

    @staticmethod
    @abstractmethod
    def get_result():
        pass
