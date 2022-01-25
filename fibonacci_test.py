# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:32:16 2022

@author: User
"""


from fibonaccii import fibonacci
import unittest


class FibonaTest(unittest.TestCase):
 	def test_in_fibona(self):
		    fibo=fibonacci(10)
		    self.assertIn(1,fibo)

        
unittest.main()