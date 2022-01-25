# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:10:50 2022

@author: User
"""

import unittest
from name import get_full_name 

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('alijon','valiyev')
        self.assertEqual(name,'Alijon Valiyev')
        
    def test_otasining_ismi(self):
        name = get_full_name('alijon','valiyev','olimovich')
        self.assertEqual(name,'Alijon Olimovich Valiyev')
        
unittest.main()





