class IO_mock:
    def __init__(self) -> None:
        self._inputs = []
        self._outputs = []

    @property
    def inputs(self):
        return self._inputs

    @property
    def outputs(self):
        return self._outputs

    def write_to_inputs(self, input_value):
        self._inputs.append(input_value)

    def input(self, message):
        self._outputs.append(message)
        return self.inputs.pop(0)

    def output(self, message):
        self._outputs.append(message)

    def clear_inputs(self):
        self._inputs.clear()

    def clear_outputs(self):
        self._outputs.clear()

    def clear(self):
        self.clear_inputs()
        self.clear_outputs()
