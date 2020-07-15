class Planets:
    def __init__(self,name,diameter,moons,year):
        self.name=name
        self.dia=diameter
        self.moon=moons
        self.days=year

    def radius(self):
        radii=0
        radii=radii+(self.dia/2)
        return radii
    def no_of_days(self):
        days=0
        days=days+(self.days)
        return days
    
def large_planet(*planets):
    large=planets[0].dia
    for i in planets:
        if i.dia>large:
            large=i.dia
    for i in planets:
        if i.dia ==large:
           print("the largest planet is: ",i.name) 
        


mer=Planets("MERCURY",4879,0,88)
v=Planets("VENUS",12100,0,225)
e=Planets("EARTH",12755,1,365)
m=Planets("MARS",6786,2,687)
j=Planets("JUPITER",142800,79,4383)
s=Planets("SATURN",120537,82,10774.875)
u=Planets("URANUS",51819,27,30681)
n=Planets("NEPTUNE",49529,14,60266.25)
large_planet(mer,v,e,m,j,s,u,n)
print("The radius of the neptune planet is: ",n.radius())
print("the number.of.days of planet Jupiter: ",j.no_of_days())
    
    
