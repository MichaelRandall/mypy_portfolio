#!/usr/local/bin/python

import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'mike'
        result = cap.cap_text(text)
        self.assertEqual(result,'Mike')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_all_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()


