# testBasic.py

from django.test import TestCase

class BasicTestCase(TestCase):
    """Quick test the the Django TestCase class."""

    def setUp(self):
        """Empty for now."""

    def test_assert(self):
        """the assert functions."""

        self.assertEqual('abc', 'abc')
        self.assertEqual(1 + 2, 3)
