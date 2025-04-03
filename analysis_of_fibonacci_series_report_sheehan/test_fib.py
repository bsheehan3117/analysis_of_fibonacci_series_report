"""A test file for the functions of the fibonacci_python file"""

import unittest
import fibonacci_python as fib

class TestFibonacciPython(unittest.TestCase):

    def test_fibonacci_iterative_python(self):
        self.assertEqual(fib.fibonacci_iterative_python(0, 0), 0)
        self.assertEqual(fib.fibonacci_iterative_python(1, 0), 1)
        self.assertEqual(fib.fibonacci_iterative_python(2, 0), 1)
        self.assertEqual(fib.fibonacci_iterative_python(10, 0), 55)

    def test_fibonacci_recursive_python(self):
        self.assertEqual(fib.fibonacci_recursive_python(0, 0), 0)
        self.assertEqual(fib.fibonacci_recursive_python(1, 0), 1)
        self.assertEqual(fib.fibonacci_recursive_python(2, 0), 1)
        self.assertEqual(fib.fibonacci_recursive_python(10, 0), 55)

    def test_fibonacci_dynamic_programming_python(self):
        self.assertEqual(fib.fibonacci_dynamic_programming_python(0, 0), 0)
        self.assertEqual(fib.fibonacci_dynamic_programming_python(1, 0), 1)
        self.assertEqual(fib.fibonacci_dynamic_programming_python(2, 0), 1)
        self.assertEqual(fib.fibonacci_dynamic_programming_python(10, 0), 55)


if __name__ == "__main__":
    unittest.main()