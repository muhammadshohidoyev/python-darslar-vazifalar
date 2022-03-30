# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:38:16 2022

@author: User
"""

import unittest 
from shaxs_talaba import Talaba

class TalabaTest(unittest.TestCase):
    def setUp(self):
        ism = "Hasan"
        familiya = "Husanov"
        tyil = 1999
        universitet = "Inha"
        bosqich = 2
        self.hobby = "futbol"
        self.talaba1 = Talaba(ism, familiya, tyil, universitet,bosqich)
        
    def test_reate(self):
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba1.universitet)
        self.assertIsNotNone(self.talaba1.bosqich)
        self.assertIsNone(self.talaba1.hobby)
        
    def test_get_info(self):
        talaba1 = "Hasan Husanov Inha universitetida 2-bosqich talabasi"
        self.assertEqual(talaba1,self.talaba1.get_info())
        
unittest.main()
        