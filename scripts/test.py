import unittest
from fib import fibonacci

def fun(x):
    return x + 1

if __name__ == "__main__":
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(fib(2), [1,2])
