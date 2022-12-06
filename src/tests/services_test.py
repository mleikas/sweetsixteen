import unittest
from services.reference_service import reference_service, UserInputError

class TestValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = reference_service
