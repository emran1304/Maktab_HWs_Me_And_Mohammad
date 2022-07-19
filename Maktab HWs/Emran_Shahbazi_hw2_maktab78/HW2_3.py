def prime(n):
    
    a = 0
    
    if n == 2:
        print('True')
        
    else:
        for i in range(2 , n):
        
        
            if n%i == 0:
                print('False')
                a += 1
                break
        
        if a == 0:
            print('True')
        

n = int(input('Please enter a number :'))
prime(n)
