# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
        
#     def get_name(self):
#         return self.ism
    
#     def get_age(self,yil):
#         return yil - self.tyil
    
#     def get_lastname (self):
#         return self.familiya
    
#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}"
        
        
# talaba1 = Talaba("Nodir","Shohidoyev",2001)    

# class User:
#     """Фойдаланувчи номли класс яратаман"""
#     def __init__(self,name,lastname,username,birth_d,email):
#         self.name = name
#         self.lastname = lastname
#         self.username = username
#         self.birth_d = birth_d
#         self.email = email
#         self.level = 2
        
        
#     def get_name(self):
#         return self.name
        
#     def get_lastname(self):
#         return self.lastname
        
#     def get_username(self):
#         return self.username
        
#     def get_age(self,age):
#         return age-self.birth_d
        
#     def det_email(self):
#         return self.email
    
#     def set_level(self, new_level):
#         self.level = new_level
        
#     def update_level(self):
#         self.level += 1
    
#     def get_info(self):
#         return f"Name:{self.name}, lastame:{self.lastname},\
#                user:{self.username}, birth_d:{self.birth_d},\
#                email:{self.email} {self.level}-nd year student"
                
# user1 = User("James","Johnson","jjohnson89",1989,"jjohnson89@gmail.com")
# user2 = User("Javier","Fernandez","jav3rf08",2000,"jav3rf08@gmail.com")

class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil


class Fan:
    """Fan nomli klass"""

    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]


matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba("Hasan", "Alimov", 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)




