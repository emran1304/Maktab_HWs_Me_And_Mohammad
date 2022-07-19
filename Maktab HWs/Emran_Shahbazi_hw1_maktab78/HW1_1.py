x = input()
x = list(x)
l = []
s = ['a' , 'i' , 'o' , 'u' , 'e' , 'A' , 'I' , 'O' , 'U' , 'E']

print(x)
for i in range(len(x)):
    
    if x[i] == ' ':
        continue
    
    
        
    if (x[i].isupper() == True):
        
        if (x[i] in s):
            l.append('.')
        else:
            l.append(x[i].lower())
        
    if (x[i].islower() == True):
        
        if (x[i] in s):
            l.append('.')
            
        else:
            l.append(x[i].upper())
        
new = ''

for i in l:
    new += i
    
print(new)
        
