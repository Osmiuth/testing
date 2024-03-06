import math
import unittest
import numpy as np


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(8, 4), 4)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 6), 30)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)

    def test_squared(self):
        self.assertEqual(squared(10), 100)
        self.assertEqual(squared(5), 25)
        self.assertEqual(squared(2), 4)
        self.assertEqual(squared(-2), 4)
        self.assertEqual(squared(-5), 25)

    def test_squareroot(self):
        self.assertEqual(squareroot(5, 3), 2.236)
        self.assertEqual(squareroot(10), 3.1622776601)
        self.assertEqual(squareroot(25), 5)
        self.assertEqual(squareroot(100), 10)


    def test_exponent(self):
        self.assertEqual(exponent(5, 2), 25)
        self.assertEqual(exponent(5, 10), 9765625)
        self.assertEqual(exponent(-3, 2), 9)
        self.assertEqual(exponent(-2, 3), -8)
        self.assertEqual(exponent(50, 2), 2500)

    def test_sine(self):
        self.assertEqual(sine(30), math.sin(30))
        self.assertEqual(sine(10), math.sin(10))
        self.assertEqual(sine(-10), math.sin(-10))
        self.assertEqual(sine(-30), math.sin(-30))

    def test_cosine(self):
        self.assertEqual(cosine(50), math.cos(50))
        self.assertEqual(cosine(10), math.cos(10))
        self.assertEqual(cosine(-10), math.cos(-10))
        self.assertEqual(cosine(-50), math.cos(-50))


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def squared(x):
    return x * x


def squareroot(num, n_dec=10): #the second argument is the amount of decimals to be displayed.
    nat_num = 1
    while nat_num ** 2 <= num:
        result = nat_num
        nat_num += 1

    for d in range(1, n_dec + 1):
        increment = 10 ** -d
        count = 1
        before = result

        while (before + increment * count) ** 2 <= num:
            result = before + increment * count
            count += 1
    return round(result, n_dec)


def exponent(x, y):
    result = pow(x, y // 2)
    result = result * result

    if y % 2 != 0:
        result = result * x
    return result

def sine(x):
    return np.sin(x)

def cosine(x):
    return np.cos(x)

if __name__ == '__main__':
    unittest.main()
