class Planet:    
    def __init__(self,name,diameter,moons,year):
        self.name=name
        self.dia=diameter
        self.no_of_moons=moons
        self.length_of_days=list(year.split(" "))

    def radius(self):
        return self.dia/2

    def no_of_days(self):
        if(self.length_of_days[1].lower()=="earth"):
            print("the number.of.days of planet",self.name," is: ",int(self.length_of_days[0])*365.25,"days")
        else:
           print("the number of days of the planet",self.name,"is: ",self.length_of_days[0],"days")
        

    
def large_planet(*planet):
    large=planet[0].dia
    for i in planet:
        if i.dia>large:
            large=i.dia
            large_planet=i
    print("the largest planet is: ",large_planet.name) 
        
    
mercury=Planet("MERCURY",4879,0,"88 days")
venus=Planet("VENUS",12100,0,"225 days")
earth=Planet("EARTH",12755,1,"365 days")
mars=Planet("MARS",6786,2,"687 days")
jupiter=Planet("JUPITER",142800,79,"12 earth years")
saturn=Planet("SATURN",120537,82,"29.5 earth years")
uranus=Planet("URANUS",51819,27,"84 earth years")
neptune=Planet("NEPTUNE",49529,14,"165 earth years")
print("The radius of the  planet is: ",neptune.radius())
jupiter.no_of_days()
large_planet(mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)    
    

    
    
