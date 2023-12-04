from abc import ABC, abstractmethod


# Factory interface
class IButtonDrawInterface(ABC):
    @abstractmethod
    def draw_button(self):
        pass
