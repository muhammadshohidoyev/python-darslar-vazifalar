# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:11:35 2022

@author: User
"""

import unittest
from max_n import max_number

class maxNumTest(unittest.TestCase):
    def test_num_max(self):
        self.assertEqual(max_number(7,27,3),27)
        self.assertEqual(max_number(56,49,33),56)
        self.assertEqual(max_number(61,72,98),98)
        
unittest.main()