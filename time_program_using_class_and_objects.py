class Time:
    def __init__(self,hours,mins):
        self.hours=hours
        self.mins=mins
    def add_times(time1,time2):
         sum=Time(0,0)
         sum.hours=time1.hours+time2.hours
         sum.mins=time1.mins+time2.mins
         if sum.mins>=60:
             sum.mins=sum.mins-60
             sum.hours=sum.hours+1
         return sum
    def time_difference(time1,time2):
         diff=Time(0,0)
         diff.hours=time1.hours-time2.hours
         diff.mins=time1.mins-time2.mins
         return diff
         
    def display_time(self):
         print("THE TIME IS",self.hours,"HRS AND",self.mins,"MINS.")
    def display_minutes(self):
        total_minutes=(self.hours*60)+(self.mins)
        print("Total Minutes=",total_minutes,"mins")



a=Time(5,50)
b=Time(2,15)
c=Time.add_times(a,b)
c.display_time()
c=Time.time_difference(a,b)
c.display_time()
c=Time.add_times(a,b)
c.display_minutes()
            
