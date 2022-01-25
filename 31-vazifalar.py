# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 12:11:39 2021

@author: User
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni = 0
    def __init__(self,ism,familiya,passport,tyil,hobby,kasb,country):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.___hobby = hobby
        self.__kasb = kasb
        self.__country = country
        Shaxs.__odamlar_soni += 1
        
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    
    def __lt__(self,y):
        return self.tyil>y.tyil
    
    def __eq__(self,y):
        return self.tyil==y.tyil
    
    # @classmethod
    # def get_odam_soni(cls):
    #     return cls.__odamlar_soni
        
    # def get_ism(self):
    #     return self.ism
    
    # def get_familiya(self):
    #     return self.familiya
    
    # def get_passport(self):
    #     return self.passport
    
    # def get_tyil(self):
    #     return self.tyil
    
    # def get_hobby(self):
    #     return self.__hobby
    
    # def get_kasb(self):
    #     return self.__kasb
    
    # def get_country(self):
    #     return self.__country
    
shaxs1 = Shaxs("Akbar","Erkinov","F11333300",1996,"Futbol","Veb dizayner","O'zbekiston")  
shaxs2 = Shaxs("Ismoil","Ikrom","F11442200",1995,"Tennis","Muhandis","O'zbekiston")   
shaxs3 = Shaxs("Olim","Temirov","F22442200",1991,"Boks","Iqtisodchi","O'zbekiston")

class Student:
    """Talabalar"""
    #__num_student = 0
    def __init__(self,name,last_name,study,age,course,passport,idnumber):
        self.name = name
        self.last_name = last_name
        self.study = study
        self.age = age
        self.course = course
        self.passport = passport
        self.idnumber = idnumber
        #Student.__num_student += 1
    
    def __repr__(self):
        return f"{self.name} {self.last_name}. Study:{self.study}. Age:{self.age}. {self.course}-course. P:{self.passport} Id:{self.idnumber}."
    
    def __ge__(self,y):
        return self.age>=y.age
    
    def __gt__(self,c):
        return self.course>c.course
    # @classmethod    
    # def get_student_num(cls):
    #     return cls.__num_student
    
    # def get_name(self):
    #     return self.name
    
    # def last_name(self):
    #     return self.last_name
    
    # def get_study(self):
    #     return self.study
    
    # def get_age(self):
    #     return self.age
    
    # def get_course(self):
    #     return self.__course
    
    # def add_course(self, course):
    #     if course >= 0:
    #         self.__course = course
    #     else: 
    #         print("This cannot be changed")
            
    
student1 = Student("Steven","Parker","University of Cambridge",18,1,"P000111222","FF111000")
student2 = Student ("Jessica","Davids","University of Oxford",19,2,"RB99870012","FF222000")
student3 = Student ("Jacob","Smith","Stanford University",20,3,"X111177000","FF33311122")  
student4 = Student("John","Thompson","University of Cambridge",20,4,"H199922330","FE1100444")
student5 = Student ("Gabriel","West","University of Oxford",19,2,"FF980011111","I00112233")
student6 = Student ("Anthony","Carragher","Stanford University",18,1,"P000221111","AA11100022")  
student7 = Student("Nico","Alvarez","University of Michigan",20,3,"FB777111000","T111100222")
    
class Fan:
    """Fan nomli klass"""
    def __init__(self,subjectName):
        self.subjectName = subjectName
        self.students = []
        
    def __len__(self):
        return len(self.students)
    
    def __getitem__(self,index):
        return self.students[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Student):
            self.students[index]=value
    
    def __add__(self,student):
        if isinstance(student,Student):
            self.students.append(student)   
            
    def __sub__(self,student):
        self.students.remove(student)
        
    def __call__(self,student):
        return [student for student in self.students]
    
    def add_student(self,*studento):
        for student in studento:
            if isinstance(student,Student):
                self.students.append(student)
            else:
                print("Enter student")
        
    
physics = Fan("Physics")   
biology = Fan("Biology")
chemistry = Fan("Chemistry")
algebra = Fan("Algebra")
physics.add_student(student1,student2,student3,student4,student5,student6,student7)
biology.add_student(student1,student2,student3,student4,student5,student6,student7)
chemistry.add_student(student1,student2,student3,student4,student5,student6,student7)
algebra.add_student(student1,student2,student3,student4,student5,student6,student7)


#student7 = Student("Nico","Alvarez","University of Michigan",20,3,"FB777111000","T111100222")






