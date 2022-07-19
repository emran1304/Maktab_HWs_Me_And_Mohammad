s = input('Please Enter a string :')
l = []

for i in s:
    if i not in l:
        
        l.append(i)
        
d = {}

for i in l:
    d[i] = 0
    
for i in s:
    d[i] += 1
    
print(d)