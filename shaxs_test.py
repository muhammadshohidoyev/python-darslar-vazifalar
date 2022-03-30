# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 10:55:02 2022

@author: User
"""
import unittest 
from shaxs_talaba import Shaxs

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
               
unittest.main()
        
        
