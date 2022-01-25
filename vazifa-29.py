# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:25:38 2021

@author: User
"""

class Car:
    
    def __init__(self,make,brand,model,color,box,price):
        self.make = make
        self.brand = brand
        self.model = model
        self.color = color
        self.box = box
        self.price = price
        self.km = 0
        
        
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.color
    
    def get_box(self):
        return self.box
    
    def get_price(self):
        return self.price
    
    def get_info(self):
        return f"{self.make}. {self.brand}. {self.model}. {self.color}. {self.box}. {self.price}. {self.km}-km."    
    
    def get_info_cars(self):
        return f"Year:{self.make}. {self.brand} {self.model}. Color: {self.color}. {self.box}. {self.price}$"
        
    def set_km(self,km):
        self.km = km
        
    def update_km(self):
        self.km += 100
        
# car1 = Car(2021,"BMW","M4","blue","auto",102770)
# car2 = Car(2021,"Mercedes Benz","Cls","black","manual",94000)    

class Autosaloon:
    
    def __init__(self,saloon_name,address):
        self.saloon_name = saloon_name
        self.address = address
        self.cars_market = 0
        self.cars = []
        
    def add_cars(self,car):
        self.cars.append(car)
        self.cars_market += 1
        
    def get_name(self):
        return self.saloon_name
    
    def get_cars(self):
        return [car.get_info_cars() for car in self.cars]
    
    def cars_num(self):
        return self.cars_market
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]
    
inform = Autosaloon("Delivery's Village","Адрес: г. Ташкент, Зангиатинский р-н, Узгариш КФЙ, Кичик Халка Йули")    
car1 = Car(2021,"Chevrolet","Cobalt","white","manual",10725)
car2 = Car(2021,"Chevrolet","Equinox","silver","manual",38462)
car3 = Car(2021,"Chevrolet","Trailblazer","black","manual",36975)
inform.add_cars(car1)
inform.add_cars(car2)
inform.add_cars(car3)
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    