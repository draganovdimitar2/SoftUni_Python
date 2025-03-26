from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Testov", "test_sound")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Test")
        self.assertEqual(self.mammal.type, "Testov")
        self.assertEqual(self.mammal.sound, "test_sound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, "Test makes test_sound")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual(result, "Test is of type Testov")

if __name__ == "__main__":
    main()
