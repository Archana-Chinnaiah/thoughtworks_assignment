class AcOption:
    def __init__(self,ac):
        self.ac_need=ac


class Car:
    def __init__(self,category,ac):
        self.__category=category
        self.ac=AcOption(ac)
        

    def set_category(self,category):
        self.__category=category

    def get_category(self):
        return self.__category
    def print_price_menu(self):
        if(self.get_category().lower()=='auto'):
            print("\nUpto 15KM     \t\t10/km \n15KM-30KM     \t\t8/km \n30 AND ABOVE     \t15/km")
        if(cab.get_category().lower()=='micro'):
            if(ac.lower()=='yes'):
                print("\nUpto 15KM     \t\t12/km \n15KM AND ABOVE     \t10/km")
            else:
                print("\nUpto 15KM     \t\t14/km \n15KM AND ABOVE     \t12/km")

        if(self.get_category().lower()=='xl'):
            if(ac.lower()=='yes'):
                print("\nUpto 15KM     \t\t14/km \n15KM AND ABOVE     \t14/km")
            else:
                print("\nUpto 15KM     \t\t15/km \n15KM AND ABOVE     \t15/km")


        


print("\t\t\t----**CAB CATEGORIES**----")
print("\n  MAXIMUM PEOPLE\t\tCATEGORY BELONGS\tAC AVAILABILITY\n\t3\t\t\t    AUTO\t\t NOT AVAILABLE\n\t4\t\t\t    MICRO\t\t AVAILABLE\n\t10\t\t\t    XL\t\t\t AVAILABLE")
category=input("\nEnter the category you need to travel from the above list: ")
while True:
    ac=input("whether you need AC? ")
    if category.lower()=='auto' and ac.lower()=='yes':
            print("AC IS NOT AVAILABLE FOR AUTO.PLEASE ENTER AGAIN")
    else:
        print("THANKS FOR ENTERING THE DETAILS")
        break
print("\nKM-RANGE  \t\tPRICE")
cab=Car(category,ac)
cab.print_price_menu()


#output of the program is:

'''
			----**CAB CATEGORIES**----

  MAXIMUM PEOPLE		CATEGORY BELONGS	AC AVAILABILITY
	3			    AUTO		 NOT AVAILABLE
	4			    MICRO		 AVAILABLE
	10			    XL			 AVAILABLE

Enter the category you need to travel from the above list: xl
whether you need AC? yes
THANKS FOR ENTERING THE DETAILS

KM-RANGE  		PRICE

Upto 15KM     		14/km 
15KM AND ABOVE     	14/km




'''
    

    
            
   

