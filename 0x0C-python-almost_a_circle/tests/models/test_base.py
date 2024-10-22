# tests/models/test_base.py

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unit tests for the Base class"""

    def test_id_auto_assignment(self):
        """Test that id is automatically assigned when not provided"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_manual_assignment(self):
        """Test that id is correctly assigned when provided"""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_mixed_id_assignment(self):
        """Test mixed id assignment (manual and automatic)"""
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 15)
        self.assertEqual(b3.id, 5)


if __name__ == '__main__':
    unittest.main()
