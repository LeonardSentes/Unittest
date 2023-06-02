import unittest
from code import Rectangle

class TestCode(unittest.TestCase):
    def test_get_area(self):
        rectangle = Rectangle(2.0, 2.0)
        self.assertEqual(rectangle.get_area(), 4.0)

    def test_get_perimeter(self):
        rectangle = Rectangle(2.0, 2.0)
        self.assertEqual(rectangle.get_perimeter(), 8.0)

    def test_vertical_orientation(self):
        rectangle = Rectangle(2.0, 3.0)
        self.assertFalse(rectangle.vertical_orientation())

if __name__ == "__main__":
    unittest.main()

