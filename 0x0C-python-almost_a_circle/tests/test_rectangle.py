import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unit test cases for the Rectangle class."""

    def test_rectangle_init(self):
        """Test proper initialization of Rectangle with all arguments."""
        r1 = Rectangle(10, 5, 2, 3, 42)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 42)

    def test_default_values(self):
        """Test initialization of Rectangle
        with default x, y, and id values.
        """
        r2 = Rectangle(8, 4)
        self.assertEqual(r2.width, 8)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_invalid_width(self):
        """Test that width raises appropriate exceptions."""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)

        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

    def test_invalid_height(self):
        """Test that height raises appropriate exceptions."""
        with self.assertRaises(TypeError):
            Rectangle(10, "5")

        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_invalid_x(self):
        """Test that x raises appropriate exceptions."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "2", 3)

        with self.assertRaises(ValueError):
            Rectangle(10, 5, -2, 3)

    def test_invalid_y(self):
        """Test that y raises appropriate exceptions."""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, "3")

        with self.assertRaises(ValueError):
            Rectangle(10, 5, 2, -3)

    def test_setters(self):
        """Test the setters and ensure they raise appropriate errors."""
        r3 = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            r3.width = 0
        with self.assertRaises(ValueError):
            r3.height = 0
        with self.assertRaises(ValueError):
            r3.x = -1
        with self.assertRaises(ValueError):
            r3.y = -1

        r3.width = 20
        self.assertEqual(r3.width, 20)
        r3.height = 30
        self.assertEqual(r3.height, 30)
        r3.x = 5
        self.assertEqual(r3.x, 5)
        r3.y = 7
        self.assertEqual(r3.y, 7)


if __name__ == '__main__':
    unittest.main()
