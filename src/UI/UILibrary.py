from UI.ui import UI

class UILibrary:
    def __init__(self) -> None:
        self.ui = UI

    def start_program(self):
        self.ui.query()

    def input_value(self, value):
        # input a value into ui
        pass

    def reference_count_should_be(self, value):
        self.input_value(4)
        # check that book IDs don't ecceed 1
        pass