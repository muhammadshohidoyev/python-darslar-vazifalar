# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:34:12 2022

@author: User
"""

import unittest 
from shaxs_talaba import Shaxs, Talaba

class ShaxsTest(unittest.TestCase):
     """Shaxs klassini tekshiruvchi test"""
     def setUp(self):
         ism = "Hasan"
         familiya = "Husanov"
         tyil = 1995
         self.shaxs1=Shaxs(ism, familiya, tyil)
         
     def test_get_info(self):
         sh_info="Hasan Husanov 1995-yilda tug'ilgan"
         self.assertEqual(sh_info,self.shaxs1.get_info())
         
     def test_isinstance(self):
         self.assertIsInstance(self.shaxs1,Shaxs)
         
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
        
    def test_isinstance(self):
        self.assertIsInstance(self.talaba1,Talaba)
        
unittest.main()