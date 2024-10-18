import unittest
from exercises.exercise1.solution import reverse_string

class TestReverseString(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

if __name__ == '__main__':
    unittest.main()
