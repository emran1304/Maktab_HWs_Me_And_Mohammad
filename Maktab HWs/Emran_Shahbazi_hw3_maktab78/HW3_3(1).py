class Book:
    
    def __init__(self , price , quantity , title):
        self.t = title
        self.p = price
        self.q = quantity
        
    def __str__(self):
        return str(f"There is {self.q} number of {self.t} with price of {self.p}")
        
        
B = Book(20000 , 143 , 'عشق سال های وبا')
print(B)