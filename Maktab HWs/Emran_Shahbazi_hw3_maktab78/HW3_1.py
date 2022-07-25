import time
from time import strftime as s
from time import localtime as l

class BirthDay:
    
    def __init__(self , year , month , day , hour):
        
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        
    def age(self):
        
        year_now = s('%Y' , l())
        month_now = s('%m' , l())
        
        if int(month_now) >= self.month: 
            year_diff = year_now - self.year

        else:
            year_diff = int(year_now) - self.year - 1
            
        return (f'Age is {year_diff} years , or {year_diff*8760} hours')
    
    def to_birthday(self):
        
        month_now = int(s('%m' , l()))
        day_now = int(s('%d' , l()))
        day_diff = self.day - day_now    
        month_diff = self.month - month_now
        if self.month >= month_now:
            
            if self.day >= day_now:
                
                return (f'{month_diff} months and {day_diff} days left to birthday')
            
            else:
                return (f'{month_diff - 1} months and {30 + day_diff} days left to birthday')
            
        else:
            return (f'{12 + month_diff - 1} months and {30 + day_diff} days left to birthday')
  
