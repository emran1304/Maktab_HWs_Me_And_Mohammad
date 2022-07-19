#### Method_1

x = input()
int_x = int(x)
x = list(x)
l = []

for i in range(len(x)):
    l.append(x[len(x) - 1 - i])
    
ans_1 = ''

for i in l:
    ans_1 += i
    
print('Method_1 Output Is : ' , int(ans_1))


#### Method_2


ans_2 = 0
 
while( int_x > 0):
    a = int_x % 10
    ans_2 = ans_2 * 10 + a
    int_x = int_x // 10
 
print('Method_2 Output Is : ' , int(ans_2))