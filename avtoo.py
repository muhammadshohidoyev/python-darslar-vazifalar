# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:12:59 2021

@author: User
"""

from uuid import uuid4


class Avto:
    """Avtomobil klassi"""

    __num_avto = 0

    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    
    
    
    def __repr__(self):
        return f"Avto: {self.make} {self.model}"
        
    # @classmethod
    # def get_num_avto(cls):
    #     return cls.__num_avto

    # def get_km(self):
    #     return self.__km

    # def get_id(self):
    #     return self.__id

    # def add_km(self, km):
    #     """Mashinaning km ga yana km qo'shish"""
    #     if km >= 0:
    #         self.__km += km
    #     else:
    #         print("Mashina km kamaytirib bo'lmaydi")

    def __eq__(self,y):
        return self.narx==y.narx
    
    def __lt__(self,y):
        return self.narx<y.narx
    
    def __le__(self,y):
        return self.narx<=y.narx

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []    
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting!")
 
salon1 = AvtoSalon("MaxAvto")    

       
avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)           
avto2 = Avto("GM","Lacetti","Oq",2020,20000,1000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
salon1.add_avto(avto1,avto2,avto3)



 
class Bus:
    pass

class Train:
    pass