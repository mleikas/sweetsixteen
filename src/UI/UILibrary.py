from ui import UI
import mock

class UILibrary:
    def __init__(self, UI:UI):
        self.ui = UI

    def start_program():
        pass

    def input_value(self, value):
        mock.patch("builtins.input", return_value = value)
  
    def reference_count_should_be(self, value):
        self.input_value(3)
        # check that book IDs don't ecceed 1
        pass

