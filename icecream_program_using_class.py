class IceCream:    
    def __init__(self,flavours,types):
        self.flavours=flavours
        self.types=types
    def display_cost(self):
        return self.flavours*self.types

class Chocolate(IceCream):
    def __init__(self,flavours,types,top=0):
        IceCream.__init__(self,flavours,types)
        self.top=top
    def display_toppings(self):   
        if((self.top)==0):
            return 1
        else:
            return (self.top)


stick=10
cone=10
cup=15
strawberry=15
chocolate=10
vanilla=10
choco_chips=5
caramel=10
nuts=15
print(" \t \t LIST OF ICECREAM FLAVOURS,TYPES AND TOPPINGS")        
print("FLAVOURS \tTYPES \tTOPPINGS \nchocolate \tstick \tchocoChips \nvanilla \tcone \tcaramel \nstrawberry \tcup \tnuts")
f=input("enter the flavour: ")
t=input("Enter the type: ")
top=input("if you need toppings,Enter the topping: else enter 0: ")
c=Chocolate(f,t,top)
print("The cost of IceCream:",c.display_toppings()*c.display_cost())

        
        
        
