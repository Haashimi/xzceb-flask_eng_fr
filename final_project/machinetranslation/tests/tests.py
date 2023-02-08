import unittest

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(englishToFrench(""), "") # null test.
        self.assertEqual(englishToFrench("Hello"), "Bonjour")  # test for the translation of the world 'Hello' and 'Bonjour'.

# class TestF2E(unittest.TestCase): 
#     def test1(self): 
#         #self.assertEqual(frenchToEnglish(""), "") # null test.
#         self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  # test for the translation of the world 'Hello' and 'Bonjour'.

unittest.main()