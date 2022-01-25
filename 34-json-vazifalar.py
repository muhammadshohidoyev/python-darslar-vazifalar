# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:46:03 2022

@author: User
"""
import json

# data = {"Model" : "Malibu", 
#         "Rang" : "Qora", 
#         "Yil":2020, 
#         "Narh":40000}

# data_json = json.dumps(data, indent=4)
# print(data_json)


# talabaa = {"ism":"Hasan",
#            "familiya":"Husanov",
#            "tyil":2000}
# talabaa_json = json.dumps(talabaa)
# print(talabaa_json)
#talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
#talaba = json.loads(talaba_json)
#print(f"{talaba['ism']} {talaba['familiya']}")


#with open('data.json','w') as f:
#    json.dump(data,f)
    
# with open('talabaa','w') as f:
#     json.dump(talabaa,f)

# with open('students.json') as f:
#     data = json.load(f)
    
# for item in data["student"]:
#     print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']}")

with open('wikipedia.json') as f:
    wiki = json.load(f)
    
print(wiki["query"]["pages"]["13801"]["title"])
print(wiki["query"]["pages"]["13801"]["extract"])
    