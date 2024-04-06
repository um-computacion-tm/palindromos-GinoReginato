#PALINDROME TEST

import unittest

def is_palindrome(mystring):
    for indice in range(len(mystring)):
        if mystring[indice] != mystring[-(indice + 1)]:
            print("no es")
            return False
    print("es")
    return True
    cleaned_string = mystring.replace(" ", "").lower()
    
    return cleaned_string == cleaned_string[::-1]

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome("AcA")
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome("ABCA")
        self.assertEqual(resultado, False)

    def test_c(self):
        resultado = is_palindrome("neuquen")
        self.assertEqual(resultado, True)

    def test_d(self):
        resultado = is_palindrome("ne uqu enL")
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()
