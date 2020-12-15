import unittest

# from Python_OOP.Unit_Testing.Test_Cat.cat import Cat
from Python_OOP.Unit_Testing.Test_Cat.cat import Cat


class TestCat(unittest.TestCase):
    def test_cat_eating(self):
        c = Cat('Misha')
        # c.fed = False
        # c.sleepy = False
        # c.size = 0
        c.eat()
        self.assertEqual(c.fed, True)
        self.assertEqual(c.size, 1)

    def test_cat_fed(self):
        c = Cat('Misha')
        c.fed = True
        with self.assertRaises(Exception) as ex:
            c.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_sleep_error(self):
        c = Cat('Misha')
        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_sleep(self):
        c = Cat('Misha')
        c.eat()
        c.sleep()
        self.assertEqual(c.sleepy, False)


if __name__ == '__main__':
    unittest.main()
