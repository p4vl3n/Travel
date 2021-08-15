import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def test_init(self):
        mammal = Mammal("John", "cat", "meow")
        self.assertEqual('John', mammal.name)
        self.assertEqual("cat", mammal.type)
        self.assertEqual('meow', mammal.sound)
        self.assertEqual(mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        mammal = Mammal("John", "cat", "meow")
        res = mammal.make_sound()
        self.assertEqual("John makes meow", res)

    def test_get_kingdom(self):
        mammal = Mammal("John", "cat", "meow")
        res = mammal.get_kingdom()
        self.assertEqual("animals", res)

    def test_info(self):
        mammal = Mammal("John", "cat", "meow")
        res = mammal.info()
        self.assertEqual("John is of type cat", res)
