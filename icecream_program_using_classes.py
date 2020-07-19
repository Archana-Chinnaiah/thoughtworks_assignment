class IceCream:    
    def __init__(self,flavours_types,topping):
        self.flavours_types=flavours_types
        self.topping=topping
    def display_cost(self):
        print("The cost of ice cream is: ",ice_cream(self.flavours_types,self.topping))

def ice_cream(flavour_type,top):
    list=flavour_type.split(" ")
    if(top.lower()=='no'):
        return cost_of_flavours.get(list[0])*cost_of_types.get(list[1])
    return cost_of_flavours.get(list[0])*cost_of_types.get(list[1])*cost_of_toppings.get(top)

cost_of_types={'stick':10,'cone':10,'cup':15}
cost_of_flavours={'strawberry':15,'chocolate':10,'vanilla':10}
cost_of_toppings={'choco_chips':5,'caramel':4,'nuts':15}


print(" \t \t LIST OF ICECREAM FLAVOURS,TYPES AND TOPPINGS")        
print("FLAVOURS \tTYPES \tTOPPINGS \nchocolate \tstick \tchocoChips \nvanilla \tcone \tcaramel \nstrawberry \tcup \tnuts")
flavour_and_type=input("\nEnter the flavour and Type of an icecream: ")
topping=input("Whether you need toppings,if 'yes',enter the toppings: ")


ice=IceCream(flavour_and_type,topping)
ice.display_cost()

        
        
        
