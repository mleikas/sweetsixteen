from ui import UI #this raises an error
import mock

class UILibrary:
    def __init__(self, UI:UI):
        self.ui = UI

    def start_program():
        """use this for starting a query or the main program if necessary"""
        pass 

    def input_value(self, value):
        """this should inject a value to a running input-command"""
        mock.patch("builtins.input", return_value = value)
  
    def reference_count_should_be(self, value):
        self.input_value(4)
        # TODO make sure only the wanted amound of references comes up,
        # for example by counting the numero of @-symbols in the parsed output
        pass

