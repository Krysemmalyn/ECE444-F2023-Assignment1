import unittest
import utils

class NumberTests(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(utils.utils.reversed(42069), 96024)
        with self.assertRaises(TypeError):
            utils.utils.reversed('hello')
        with self.assertRaises(TypeError):
            utils.utils.reversed(420.69)

    def test_formatter(self):
        self.assertEqual(utils.utils.formatter(365), ('0b101101101', '0o555'))
        with self.assertRaises(TypeError):
            utils.utils.reversed('hello')
        with self.assertRaises(TypeError):
            utils.utils.reversed(420.69)

if __name__ == '__main__':
    unittest.main()