import unittest
import string
from generator import Password

class TestPassword(unittest.TestCase):
    def test_length(self):
        # Test to make sure the length is the same as what's passed in #
        pw = Password()
        pw.generatePassword(10)
        self.assertEqual(len(pw.password), 10)

    def test_min_length(self):
        # Tests to ensure it can't generate too short of a password
        pw = Password()
        pw.generatePassword(7)
        self.assertEqual(pw.password, "")

    def test_max_length(self):
        # Tests to ensure it can't be too long
        pw = Password()
        pw.generatePassword(95)
        self.assertEqual(pw.password, "")
        pass

    def test_has_capital(self):
        # Tests to ensure it has a capital
        pw = Password()
        pw.generatePassword(10)
        self.assertTrue(any(char.isupper() for char in pw.password))

    def test_has_lowercase(self):
        # Tests to ensure it has a lowercase
        pw = Password()
        pw.generatePassword(10)
        self.assertTrue(any(char.islower() for char in pw.password))

    def test_has_number(self):
        # Tests to ensure it has a number
        pw = Password()
        pw.generatePassword(10)
        self.assertTrue(any(char.isdigit() for char in pw.password))

    def test_has_punctuation(self):
        # Tests to ensure it has a non-alpha numeric character in two different ways, regex and alnum
        pw = Password()
        pw.generatePassword(10)
        self.assertTrue(
            any(c in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" for c in pw.password)
        )
        self.assertFalse(pw.password.isalnum())

    def test_character_uniqueness(self):
        # Tests to ensure that every character is unique by creating a set from the characters and checking the length of that
        pw = Password()
        pw.generatePassword(10)
        self.assertTrue(len(pw.password) == len(set(pw.password)))

    def test_no_consecutive_characters(self):
        # Tests to ensure that no adjacent / consecutive characters are the same
        pw = Password()
        pw.generatePassword(20)
        for i in range(len(pw.password) - 1):
            self.assertTrue(pw.password[i] != pw.password[i + 1])
            
    def test_randomization(self):
        # Tests to ensure that two generated passwords aren't identical
        pw = Password()
        pw2 = Password()
        
        pw.generatePassword(20)
        pw2.generatePassword(20)
        
        self.assertTrue(pw.password != pw2.password) 

if __name__ == "__main__":
    unittest.main()
