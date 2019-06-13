import unittest

def f1(x):
    return x+1

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(f1(3),4)


if __name__ =='__main__':
    unittest.main()