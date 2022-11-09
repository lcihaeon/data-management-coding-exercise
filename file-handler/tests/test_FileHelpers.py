import unittest
from ..helpers.FileHelpers import *


class TestFileHelpers(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_get_file_type_returns_trigger(self):
        f_type = get_file_type('')
        self.assertEqual(f_type, "TRG")


if __name__ == '__main__':
    unittest.main()
