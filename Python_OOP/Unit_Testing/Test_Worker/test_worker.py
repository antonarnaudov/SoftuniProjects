import unittest

from Python_OOP.Unit_Testing.Test_Worker.worker import Worker


class TestWorker(unittest.TestCase):
    def test_initialize(self):
        w = Worker('Ivan', 1300, 100)
        self.assertEqual('Ivan', w.name)
        self.assertEqual(1300, w.salary)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)

    def test_work_raises(self):
        w = Worker('Ivan', 1300, -10)
        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_work_money(self):
        w = Worker('Ivan', 1300, 100)
        w.work()
        self.assertEqual(w.money, w.salary)
        w.work()
        self.assertEqual(w.money, w.salary * 2)

    def test_work_passes(self):
        w = Worker('Ivan', 1300, 100)
        w.work()
        self.assertEqual(w.energy, 99)

    def test_rest(self):
        w = Worker('Ivan', 1300, 99)
        w.rest()
        self.assertEqual(w.energy, 100)

    def test_get_info_method(self):
        w = Worker('Ivan', 1300, 100)
        self.assertEqual(w.get_info(), f'{w.name} has saved {w.money} money.')


if __name__ == '__main__':
    unittest.main()
