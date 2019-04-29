import unittest, sys

from a25 import add_linked_list, add_linked_list_1, number_to_linked_list
from helpers import Node, list_to_linked_list

class Test25(unittest.TestCase):

    def test_1(self):

        number1 = list_to_linked_list([7, 1, 6])
        number2 = list_to_linked_list([5, 9, 2])
        result = add_linked_list(number1, number2)
        self.assertEqual(result, 912)

        number1 = list_to_linked_list([7, 1, 6, 2])
        number2 = list_to_linked_list([5, 9, 2])
        result = add_linked_list(number1, number2)
        self.assertEqual(result, 2912)

    def test_2(self):

        number1 = list_to_linked_list([7, 1, 6])
        number2 = list_to_linked_list([5, 9, 2])
        result = add_linked_list_1(number1, number2)
        self.assertEqual(result, 912)

        number1 = list_to_linked_list([7, 1, 6, 2, 1])
        number2 = list_to_linked_list([5, 9, 2])
        result = add_linked_list_1(number1, number2)
        self.assertEqual(result, 12912)

        result = add_linked_list_1(number2, number1)
        self.assertEqual(result, 12912)

if __name__ == '__main__':
    unittest.main()
