# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:18:21 2022

# @author: User
"""
import unittest
from evennum import even

class Even(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even([8,9,10,11,12]),[8,10,12])
        
unittest.main()        