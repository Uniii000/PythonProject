from abc import ABC, abstractmethod
from Interfaces.ButtonDrawInterface import IButtonDrawInterface
from ButtonsFactoryPattern.Buttons.LoadButton import LoadButton
from ButtonsFactoryPattern.Buttons.StartButton import StartButton
from ButtonsFactoryPattern.Buttons.StopButton import StopButton
from ButtonsFactoryPattern.Buttons.SaveButton import SaveButton


# Factory Class
class ButtonFactoryClass(ABC):
    @abstractmethod
    def CreateButton(self):
        return IButtonDrawInterface


class StartButtonFactory(ButtonFactoryClass):
    def CreateButton(self) -> IButtonDrawInterface:
        return StartButton()


class StopButtonFactory(ButtonFactoryClass):
    def CreateButton(self) -> IButtonDrawInterface:
        return StopButton()


class SaveButtonFactory(ButtonFactoryClass):
    def CreateButton(self) -> IButtonDrawInterface:
        return SaveButton()


class LoadButtonFactory(ButtonFactoryClass):
    def CreateButton(self) -> IButtonDrawInterface:
        return LoadButton()
