#TEST PALINDROME

import unittest

def is_palindrome(mystring):
    for indice in range(len(mystring)):
        print(mystring (indice) + " -> " + mystring[-(indice +1)])
        if mystring[indice] != mystring[-(indice +1)]:
            print("no es")
            return False
        return True 

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome("AcA")
        self.assertEqual(resultado, True)

    def test_a(self):
        resultado = is_palindrome("ABCAC")
        self.assertEqual(resultado, True)


class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome("neuquen")
        self.assertEqual(resultado, True)

    def test_a(self):
        resultado = is_palindrome("neuqu en")
        self.assertEqual(resultado, True)


unittest.main()
