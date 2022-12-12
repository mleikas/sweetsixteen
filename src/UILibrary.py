import mock
from UI.ui import UI
from io_mock import IO_mock


class UILibrary:
    def __init__(self):
        self.io = IO_mock()
        self.ui = UI(self.io)

    def start_program(self):
        self.ui.query()

    def input_value(self, value):
        self.io.write_to_inputs(value)

    def input_multiple_values(self, values):
        for value in values:
            self.io.write_to_inputs(value)

    def output_should_contain(self, value):
        if not value in self.io.outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(self.io.outputs)}"
            )
