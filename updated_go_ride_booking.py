class AcOption:
    def __init__(self,ac_need,km_range,price_per_km):
        self.ac=ac_need
        self.km_range=km_range
        self.price_per_km=price_per_km
        
class CabCategory:
    def __init__(self,name,people_accomadate,ac_need,km_range,price_per_km):
        self.name=name
        self.people_accomadate=people_accomadate
        self.ac_obj=AcOption(ac_need,km_range,price_per_km)

    def price_menu_list(list,input_name,ac_input):
        for j in list:
            if j.name.lower()==input_name and j.ac_obj.ac.lower()==ac_input:
                print('\n',input_name.upper(),'\t',j.ac_obj.km_range,' \t',j.ac_obj.price_per_km)
                
def get_original_category():
    original_category=[]
    people_accomadate=[]
    result=[]
    for category in category_of_vehicles:
        original_category.append(category.name)
        people_accomadate.append(category.people_accomadate)
    original_category = list(dict.fromkeys(original_category))
    people_accomadate=list(dict.fromkeys(people_accomadate))
    result.extend([list(i) for i in zip(original_category,people_accomadate)])
    return result    
        

def display_category():
    for i in original_category:
        print(i[0],'-',i[1])

def filter_category(category):
    filtered_type = next((i for i in category_of_vehicles if i.name.lower() == category), None)
    return filtered_type


def filter_options(ac):
    filtered_type = next((i for i in category_of_vehicles if i.name.lower() == category_name and i.ac_obj.ac==ac), None)
    return filtered_type


def get_category():
    while True:
         category=input("Select a Category: ").lower()
         category_option=filter_category(category)
         if category_option is None:
             print("invalid selection")
         else:
             break
    return category  



def get_ac_need():
    while True:
         ac=input("whether you need AC? ").lower()
         ac_option=filter_options(ac)
         if ac_option is None:
             print("invalid selection")
         else:
             break
    return ac          
            

auto1=CabCategory('Auto',3,'yes','upto 15km',10)
auto2=CabCategory('Auto',3,'yes','15-30km',8)
auto3=CabCategory('Auto',3,'yes','above 30km',15)

micro_with_ac1=CabCategory('Micro',4,'yes','upto 15km',12)
micro_with_ac2=CabCategory('Micro',4,'yes','above 15km',10)
micro_without_ac1=CabCategory('Micro',4,'no','upto 15km',14)
micro_without_ac2=CabCategory('Micro',4,'no','above 15km',12)

xl_with_ac1=CabCategory('Xl',10,'yes','upto 15km',14)
xl_with_ac2=CabCategory('Xl',10,'yes','above 15km',14)
xl_without_ac1=CabCategory('Xl',10,'no','upto 15km',15)
xl_without_ac2=CabCategory('Xl',10,'no','above 15km',15)

category_of_vehicles=[auto1,auto2,auto3,micro_with_ac1,micro_with_ac2,micro_without_ac1,micro_without_ac2,xl_with_ac1,xl_with_ac2,xl_without_ac1,xl_without_ac2]

print("\n\t\t\t  ----**CAB CATEGORIES**----")

original_category=(get_original_category())

display_category()

category_name=get_category()
ac=get_ac_need()


print('\nCAB \tKM-RANGE \tPRICE PER KM')
CabCategory.price_menu_list(category_of_vehicles,category_name,ac)


