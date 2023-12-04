import json
import numpy as np


# Created for Save and load logic implementation
class SaveAndLoadClass:
    def __init__(self, game_state):
        self.game_state = game_state

    def save_game(self):
        with open("Data/save.json", "w") as file:
            json.dump(self.game_state.tolist(), file)

    def load_game(self):
        try:
            with open("Data/save.json", "r") as file:
                loaded_state = np.array(json.load(file))
                if loaded_state.shape == self.game_state.shape:
                    np.copyto(self.game_state, loaded_state)
                else:
                    print("Invalid file format. Unable to load game state.")
        except FileNotFoundError:
            print("No saved game state found.")
