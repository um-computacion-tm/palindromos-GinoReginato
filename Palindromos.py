#TEST PALINDROME

import unittest

def is_palindrome(mystring):
    # Eliminar espacios en blanco y convertir a minúsculas
    clean_string = ''.join(mystring.lower().split())

    # Comparar la cadena original con su reverso
    return clean_string == clean_string[::-1]
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