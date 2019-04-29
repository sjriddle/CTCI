import unittest, sys

from a11 import is_unique, is_unique_1, is_unique_2

class Test24(unittest.TestCase):

    def test(self):
      self.assertTrue(is_unique('abcd'))
      self.assertFalse(is_unique('aab'))
      self.assertTrue(is_unique('qwertyuiop[]'))
      self.assertFalse(is_unique('abcdedk'))


if __name__ == '__main__':
    unittest.main()
