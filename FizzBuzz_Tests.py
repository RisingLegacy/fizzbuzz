import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_one_returns_one(self):
        self.assertEqual('1', fizzbuzz(1))

    def test_two_returns_two(self):
        self.assertEqual('2', fizzbuzz(2))

    def test_three_returns_fizz(self):
        self.assertEqual('fizz', fizzbuzz(3))

    def test_five_returns_buzz(self):
        self.assertEqual('buzz', fizzbuzz(5))

    def test_six_returns_fizz(self):
        self.assertEqual('fizz', fizzbuzz(6))

    def test_ten_returns_buzz(self):
        self.assertEqual('buzz', fizzbuzz(10))

    def test_fifteen_returns_fizzbuzz(self):
        self.assertEqual('fizzbuzz', fizzbuzz(15))



