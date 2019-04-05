import unittest
from lab1 import *

# A few test cases.  Add more!!!


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """test max_list_iter"""
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([1]), 1)
        self.assertEqual(max_list_iter([1, 20, 3, 4, 5, 6]), 20)
        self.assertEqual(max_list_iter([1, 2, 3, 4, 6, 6]), 6)
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        """test test_reverse_rec"""
        tlist = None
        self.assertEqual(reverse_rec([]), None)
        self.assertEqual(reverse_rec([1]), [1])
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([1, 2, 3, 4]), [4, 3, 2, 1])
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        """test bin_search"""
        tlist = None
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(4, len(list_val)-1, 0, list_val), -1)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, []), 0)
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)


if __name__ == "__main__":
    unittest.main()

