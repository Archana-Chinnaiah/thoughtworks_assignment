import re
class Owner:
    def __init__(self,name,age,license_number,license_validity):
        self.__name=name
        self.__age=age
        self.__l_number=license_number
        self.__l_validity=license_validity

    def set_name(self,name):
        self.__name=name

    def set_age(self,age):
        self.__age=age

    def set_l_number(self,l_number):
        self.__l_number=l_number

    def set_l_validity(self,l_validity):
        self.__l_validity=l_validity



    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_l_number(self):
        return self.__l_number

    def get_l_validity(self):
        return self.__l_validity
    
    


class Car:
    def __init__(self,category,number,color,company,model,o_name,o_age,license_no,license_validity):
        self.__category=category
        self.__number=number
        self.__color=color
        self.__company=company
        self.__model=model
        self.__owner=Owner(o_name,o_age,license_no,license_validity)

    def set_category(self,category):
        self.__category=category

    def set_number(self,number):
        self.__number=number

    def set_color(self,color):
        self.__color=color
        
    def set_company(self,company):
        self.__company=company

    def set_model(self,model):
        self.__model=model

    def set_owner(self,owner):
        self.__owner=owner
  


    def get_category(self):
        return self.__category

    def get_number(self):
        return self.__number    

    def get_color(self):
        return self.__color
      
    def get_company(self):
        return self.__company
    
    def get_model(self):
        return self.__model
    
    def get_owner(self):
        return self.__owner

owner_name=input("Enter the Owner Name:").upper()
owner_age=input("Enter the Owner Age:")
while True:
    owner_license_number=input("Enter the Owner License Number:")
    if(re.match(r'(^(([A-Z]{2}[0-9]{2})( )|([A-Z]{2}-[0-9]{2}))((19|20)[0-9][0-9])[0-9]{7}$)',owner_license_number)):
        break
    else:
        print("INVALID LICENSE NUMBER")

while True:
    owner_license_validity=input("Enter the Owner License Validity in dd/mm/yyyy:")
    if(re.match(r'(^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$)',owner_license_validity)):
        break
    else:
        print("INVALID LICENSE")        

car_category=input("Enter the Car category (if MAX is 4 people -- MICRO. else if Max is 10 people --XL) -: ")
car_number=input("Enter the Car Number:")
car_color=input("Enter the Car Color:")
car_company=input("Enter the Car Company:").title()
car_model=input("Enter the Car Model:")

car=Car(car_category,car_number,car_color,car_company,car_model,owner_name,owner_age,owner_license_number,owner_license_validity)
print("\n\t\t****CAR DETAILS****\n")
print("Car category- ",car.get_category())
print("Car number- ",car.get_number())
print("Car color- ",car.get_color())
print("Car company- ",car.get_company())
print("Car model- ",car.get_model())
print("Owner name- ",car.get_owner().get_name())
print("Owner age- ",car.get_owner().get_age())
print("Owner license number- ",car.get_owner().get_l_number())
print("Owner license validity- ",car.get_owner().get_l_validity())


        

        
