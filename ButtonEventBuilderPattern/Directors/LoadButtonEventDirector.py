from ButtonEventBuilderPattern.ButtonEventBuilder import Builder
from Data import data


class LoadButtonEventDirector:
    @staticmethod
    def construct():
        return Builder() \
            .set_button_x(data.load_button_x) \
            .set_button_y(data.load_button_y) \
            .set_button_width(data.button_width) \
            .set_button_height(data.button_height) \
            .get_result()