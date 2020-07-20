class Product:
    def __init__(self,id,name,price,category):
        self.id=id
        self.name=name
        self.price=price
        self.category=category
        
    def normal_tax(self):
         if(self.price>500):
             tax=(float(self.price)*0.05)
             return tax
         
         else:
             tax=(float(self.price)*0.02)
             return tax


class DairyProduct(Product):
    def __init__(self,id,name,price,category):
        Product.__init__(self,id,name,price,category)
    def dairy_tax(self):    
        if(self.price>=1000):
           tax=float(self.price)*0.03
           return tax
        else:
            tax=0
            return tax


class TextileProduct(Product):
    def __init__(self,id,name,price,category):
        Product.__init__(self,id,name,price,category)
    def tax_for_textile(self):    
        return (float(self.price)*0.01)
        
        


# USER INPUT

print("\n\t\t****CALCULATING THE TAX FOR THE PRODUCT****\n")

id=int(input("Enter the ID for the Product: "))
name=input("Enter the NAME for the Product: ")
price=float(input("Enter the PRICE for the Product: "))
category=input("Enter the CATEGORY for the Product(HOME NEEDS,PRODUCE,DAIRY,TEXTILES): ")


if(category.lower()=="dairy"):
    dairy=DairyProduct(id,name,price,category)
    print("The tax for the product",name,"is",dairy.dairy_tax())
elif(category.lower()=="dairy"):
    textile=TextileProduct(id,name,price,category)
    print("The Tax for the product",name," is",textile.tax_for_textile()+textile.normal_tax())
else:
    product=Product(id,name,price,category)
    print("The tax for the product",name,"is",product.normal_tax())


