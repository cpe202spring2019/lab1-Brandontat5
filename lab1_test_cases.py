import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        self.assertEqual(max_list_iter([1]), 1)
        self.assertEqual(max_list_iter([1, 20, 3, 4, 5, 6]), 20)
        self.assertEqual(max_list_iter([1, 2, 3, 4, 6, 6]), 6)

    def test_max_list_iter_empty_list(self):
        self.assertEqual(max_list_iter([]), None)

    def test_max_list_iter_none_list(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([1, 2]), [2, 1])
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_reverse_rec_empty_list(self):
        self.assertEqual(reverse_rec([]), None)

    def test_reverse_rec_none_list(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)
        self.assertEqual(bin_search(4, len(list_val)-1, 0, list_val), -1)

    def test_bin_search_empty_list(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, []), None)

    def test_bin_search_rec_none_list(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 5, tlist)


if __name__ == "__main__":
    unittest.main()

