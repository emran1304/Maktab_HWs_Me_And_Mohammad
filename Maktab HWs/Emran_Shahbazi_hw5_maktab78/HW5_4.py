class Add:
    
    def __init__(self, v):
        self.v = v
        
    def __call__(self, a = 0):
        x = self.v + a
        w = Add(x)
        
        return w
    
    def __str__(self):
        return str(self.v)
    
print(Add(5)(10)(20))

