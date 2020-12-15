import unittest

from Python_OOP.Unit_Testing.Test_List.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):
    def _test_init(self):
        with self.assertRaises(Exception) as ex:
            IntegerList(1, 2, 3, '4', 5, 6, 7, 8)
        self.assertIsNotNone(ex.exception)

    def test_get_data(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8]
        ll = IntegerList(*values)

        self.assertEqual(ll.get_data(), values)

    def test_add_pass(self):
        ll = IntegerList()
        ll.add(1)

        self.assertListEqual([1], ll.get_data())

    def test_add_exception(self):
        ll = IntegerList()
        with self.assertRaises(Exception) as ex:
            ll.add('1')
        self.assertIsNotNone(ex.exception)

    def test_remove_index_pass(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        initial_length = len(ll.get_data())

        ll.remove_index(2)
        after_removal_length = len(ll.get_data())

        self.assertEqual(initial_length - 1, after_removal_length)

    def test_remove_index_exception(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        with self.assertRaises(IndexError) as index_error:
            ll.remove_index(9)
        self.assertEqual(str(index_error.exception), "Index is out of range")

    def test_get_pass(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(ll.get(1), ll.get_data()[1])

    def test_get_exception(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        with self.assertRaises(IndexError) as index_error:
            ll.get(9)
        self.assertEqual(str(index_error.exception), "Index is out of range")

    def test_insert_pass(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        ll.insert(0, 9)
        self.assertEqual(ll.get(0), 9)

    def test_insert_index_error(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        with self.assertRaises(IndexError) as index_error:
            ll.insert(9, 9)
        self.assertEqual(str(index_error.exception), "Index is out of range")

    def test_insert_value_error(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        with self.assertRaises(ValueError) as value_error:
            ll.insert(1, '9')
        self.assertEqual(str(value_error.exception), "Element is not Integer")

    def test_get_biggest(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(ll.get_biggest(), 8)

    def test_get_index(self):
        ll = IntegerList(1, 2, 3, 4, 5, 6, 7, 8)
        self.assertEqual(ll.get_index(4), 3)


if __name__ == '__main__':
    unittest.main()
