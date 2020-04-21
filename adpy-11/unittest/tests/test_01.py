import unittest
import my_app

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(my_app.summa(5,5),10)


if __name__ == '__main__':
    unittest.main()
