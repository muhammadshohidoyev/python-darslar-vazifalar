# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:52:00 2022

@author: User
"""

import unittest
from bigletter import letter_title
    
class BigLetterTest(unittest.TestCase):
    def test_letter_title(self):
        self.assertEqual(letter_title(['hello','world']),['Hello','World'])
        self.assertEqual(letter_title(['artificial','intelligence']),['Artificial','Intelligence'])

unittest.main()