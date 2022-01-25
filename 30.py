# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:57:30 2021

@author: User
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
     
    
inson = Shaxs("Hasan","Rustamov","F111100222",1993)
#print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")    
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)   
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        
        
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def fanga_yozil(self,fan_nomi):
        self.fanlar.append(fan_nomi)
    
    def remove_fan(self,fan_nomi):
        for fan in self.fanlar:
            if fan == fan_nomi:
                self.fanlar.remove(fan)
            else: 
                return f"Siz {fan_nomi.get_fanNomi()} faniga yozilmagansiz"
        
    def get_fanlar(self):
        return [fan.get_fanNomi() for fan in self.fanlar]

        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()}-bosqich. Id raqami: {self.idraqam}"
        info += f"Fanlar: {self.get_fanlar()}"
        return info
    


#talaba1= Talaba("Valijon Rasulov","Aliyev","FA112299",1996,"000011333")             
    
class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


talaba1_manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")
talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil)    


class Fan:
    """Fan klassi"""
    def __init__(self,fanNomi):
        self.fanNomi = fanNomi
    
    def get_fanNomi(self):
        return self.fanNomi
    

fizika = Fan("Fizika")   
biologiya = Fan("Biologiya")
kimyo = Fan("Kimyo")
algebra = Fan("Algebra")
talaba1.fanga_yozil(fizika)
talaba1.fanga_yozil(biologiya)
talaba1.fanga_yozil(kimyo)
talaba1.fanga_yozil(algebra)

class User(Shaxs):
    """User class"""
    def __init__(self,ism,familiya,passport,tyil,email,tel_raqam,millat,jins):
        """User xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)   
        self.ism = ism        
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.email = email
        self.tel_raqam = tel_raqam
        self.millat = millat
        self.jins = jins
        
    def get_ism(self):
        return self.ism
    
    def get_familiya(self):
        return self.familiya
    
    def get_passport(self):
        return self.passport
    
    def get_tyil(self):
        return self.tyil
    
    def get_email(self):
        return self.email
    
    def get_tel(self):
        return self.tel_raqam
    
    def get_millat(self):
        return self.millat
    
    def get_jins(self):
        return self.jins
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. Passport: {self.passport}. {self.tyil}-yilda tug'ilgan. "
        info += f"Email: {self.email}. Tel: {self.tel_raqam}. Millati: {self.millat}. Jinsi: {self.jins}."
        return info 
    
user1 = User("Jobir","Akbarov","FF9990011",1988,
        "JAkbar@gmail.com","+998973748778","o'zbek","Erkak")
        

class Programmer(Shaxs):
    """Programmer klassi"""
    def __init__(self,ism,familiya,passport,tyil,profession,learned,work):
        
        super().__init__(ism, familiya, passport, tyil) 
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.profession = profession
        self.learned = learned
        self.work = work
        
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_passpott(self):
        return self.passport
    
    def get_d_o_b(self):
        return self.tyil
    
    def get_professsion(self):
        return self.profession
    
    def get_learned(self):
        return self.learned
    
    def get_work(self):
        return self.work
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. Passport: {self.passport}. {self.tyil}-yilda tug'ilgan. "
        info += f"Kasbi: {self.profession}. {self.learned}da o'qigan. {self.work}da ishlaydi."
        return info
programmer1 = Programmer("Umar","Umarov","FF777788001990",1990,"Software engineer",
                          "Massachusetts Institute of Technology","Google")   
    
class Admin(User):
    """Admin klassi"""
    def __init__(self,ism, familiya, passport, tyil, email, tel_raqam, millat, jins):
        super().__init__(ism, familiya, passport, tyil, email, tel_raqam, millat, jins)  
        
        
    def ban_user(self):
        return f"{self.ism} bloklandi"
        
bloklangan_user = Admin("Erkin","To'lqinov","N000111222",1998,"Erikwave97@gmail.com","+998909788899","o'zbek","Erkak")       
    
    
    
    
    
    
    
    
    
    
    
    
    
    











    
    