# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:12:02 2022

@author: User
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_info(self):
            return f"{self.ism.title()} {self.familiya.title()} {self.tyil}-yilda tug'ilgan"

shaxs1 = Shaxs("hasan","husanov",1995)

class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, tyil, universitet, bosqich, hobby=None):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, tyil)
        self.universitet = universitet
        self.bosqich = bosqich 
        self.hobby = hobby
        
    def get_universitet(self):
            return self.universitet
        
    def set_bosqich(self,n):
            self.bosqich = n
            return self.bosqich
    
    def get_info(self):
            if self.hobby:
                    return f"{self.ism.title()} {self.familiya.title()} {self.universitet.title()} universitetida {self.bosqich}-bosqich talabasi, {self.hobby}ga qiziqadi"
            else:    
                    return f"{self.ism.title()} {self.familiya.title()} {self.universitet.title()} universitetida {self.bosqich}-bosqich talabasi"
                
talaba1 = Talaba("hasan","husanov",1999,"inha",2,"futbol")
talaba1.set_bosqich(3)