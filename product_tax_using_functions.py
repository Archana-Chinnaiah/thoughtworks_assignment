def shop_list(id,name,price,category):
 if(category.lower()=="dairy"):
    if(price>=1000):
        tax=0
        tax=tax+price*0.03
        print("The Tax for the product",name," is",tax)
    else:
        tax=0
        print("The Tax for the product",name," is",tax)
 else:
     if(price>500):
         tax=0
         tax=tax+(price*0.05)
         if(category.lower()=="textiles"):
             tax=tax+(price*(0.01))
         print("The Tax for the product",name," is",tax)
     elif(price<=500):
         tax=0
         tax=tax+(price*0.02)
         if(category.lower()=="textiles"):
             tax=tax+(price*(0.01))
         print("The Tax for the product",name," is",tax)

  
shop_list(11,"Milk",100,"dairy")
shop_list(12,"butter",2000,"Dairy")
shop_list(15,"chocolate",5000,"Dairy")
shop_list(13,"saree",3000,"Textiles")
shop_list(14,"T-shirt",490,"Textiles")
shop_list(15,"Fruits",200,"Produce")
shop_list(16,"Vegetables",200,"Produce")
shop_list(17,"Fan",200,"Home Needs")
shop_list(18,"T.v",200,"Home Needs")

# GETTING USER INPUT
'''
id=int(input("Enter the ID for the Product: "))
name=input("Enter the Name for the Product: ")
price=float(input("enter the price for the product"))
category=input("enter the Category that the product belongs(DAIRY,PRODUCE,HOME NEEDS,TEXTILES): ")
shop_list(id,name,price,category)
'''
