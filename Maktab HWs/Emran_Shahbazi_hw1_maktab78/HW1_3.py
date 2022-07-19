l = input()
l = list(l)
w = ['[' , ']' , "'" , ',']

duplicates_removed = []

for i in l:
    if i in w:
        continue
    else:
        
        if i not in duplicates_removed:
            duplicates_removed.append(i)
            
print(duplicates_removed)
            




