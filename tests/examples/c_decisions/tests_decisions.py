import unittest

from homework.c_decisions.decisions import is_number_even, is_vowel
from src.examples.c_decisions.decisions import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_is_vowel(self):
        self.assertEqual(True, is_vowel('a'))
        self.assertEqual(True, is_vowel('e'))   
        self.assertEqual(True, is_vowel('i'))
        self.assertEqual(True, is_vowel('o'))
        self.assertEqual(True, is_vowel('u'))

    #def test_is_consonant(self):

    def test_is_number_even(self):
        self.assertEqual(True, is_number_even(2))

    def test_compare_letters(self):
        self.assertEqual(False, 'A' == 'a')
        self.assertEqual(True, 'a' == 'a')
        self.assertEqual(True, 'A' == 'A')
        
    def test_compare_words(self):
        self.assertEqual(True, 'python' == 'python')
        self.assertEqual(True, 'python' == 'pythoN')

    def test_get_generations(self):
        self.assertEqual('The Greatest Generation', get_generation(1915))
        self.assertEqual('The silent generation', get_generation(1305))
        self.assertEqual('The Greatest Generation', get_generation(1940))
