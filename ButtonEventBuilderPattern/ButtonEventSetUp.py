from Data import data
from LoadingAndSaving.SaveAndLoad import SaveAndLoadClass
from ButtonEventBuilderPattern.Directors import StartButtonEventDirector, StopButtonEventDirector, SaveButtonEventDirector, \
    LoadButtonEventDirector

# Class that contains everything
class EventSetUpClass:
    def __init__(self, event, game_state):
        self.game_state = game_state
        self.event = event
        self.start = StartButtonEventDirector.StartButtonEventDirector.construct()
        self.stop = StopButtonEventDirector.StopButtonEventDirector.construct()
        self.save = SaveButtonEventDirector.SaveButtonEventDirector.construct()
        self.load = LoadButtonEventDirector.LoadButtonEventDirector.construct()

    def EventListener(self):
        if self.EventSetUpChecker(self.start):
            data.running_simulation = True
        elif self.EventSetUpChecker(self.stop):
            data.running_simulation = False
        elif self.EventSetUpChecker(self.save):
            # Loading and saving ==================================================
            SaveAndLoadClass(self.game_state).save_game()
        elif self.EventSetUpChecker(self.load):
            SaveAndLoadClass(self.game_state).load_game()
            # =====================================================================
        else:
            x, y = self.event.pos[0] // data.cell_width, self.event.pos[1] // data.cell_height
            self.game_state[x, y] = not self.game_state[x, y]

    def EventSetUpChecker(self, button_event):
        button_x = button_event.get_button_x()
        button_y = button_event.get_button_y()
        button_width = button_event.get_button_width()
        button_height = button_event.get_button_height()

        if (
                button_x <= self.event.pos[0] <= button_x + button_width
                and button_y <= self.event.pos[1] <= button_y + button_height
        ):
            return True
