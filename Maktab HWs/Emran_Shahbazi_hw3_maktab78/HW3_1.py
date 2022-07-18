import time
from time import strftime as s
from time import localtime as l

class BirthDay:
    
    def __init__(self , year , month , day , hour):
        
        self.y = year
        self.m = month
        self.d = day
        self.h = hour
        
    def age(self):
        
        y1 = s('%Y' , l())
        m1 = s('%m' , l())
        #d1 = s('%d' , l())
        #h1 = s('%H' , l())
        
        if m1 >= self.m : 
            y2 = y1 - self.y

        else:
            y2 = y1 - self.y - 1
            
        return (f'Age is {y2} years , or {y2*8760} hours')
    
    def to_birthday(self):
        
        m1 = int(s('%m' , l()))
        d1 = int(s('%d' , l()))
        d2 = self.d - d1    
        m2 = self.m - m1
        if self.m >= m1:
            
            if self.d >= d1:
                
                return (f'{m2} months and {d2} days left to birthday')
            
            else:
                return (f'{m2 - 1} months and {30 + d2} days left to birthday')
            
        else:
            return (f'{12 + m2 - 1} months and {30 + d2} days left to birthday')
                
        
