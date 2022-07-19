def compress(a):
    
    l = list(a)
    d = {}
    code = ''
    
    
    for i in l:
        d[i] = 0
        
    for i in l:
        d[i] += 1
        
    for i in l:
        if i not in code:
            code += i
            
    for i in d.values():
        
        if i > 1:
         code += str(i)
        
    l_prime =[]
    
    for i in code:
        l_prime.append(int(i))
        
    l_prime.sort()
    code_prime = ''
    
    for i in l_prime:
        code_prime += str(i)
        
    
    return code_prime
    



def dk_coding(s):
    
    code_1 = compress(s)
    code_2 = compress(code_1)
    
    while code_1 != code_2:
        
        code_1 = code_2
        code_2 = compress(code_2)
        
    
    return code_2        
     
    
n = input('Please enter a serial number :')
print(dk_coding(n))      


