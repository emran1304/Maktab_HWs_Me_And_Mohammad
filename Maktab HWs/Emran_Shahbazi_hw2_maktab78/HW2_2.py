'''
اعداد درون لیست ، تک تک توسط کاربر به لیست اضافه میشن

'''

from functools import reduce

n = int(input('Please enter length of list :'))
l = []

for i in range(n):
    x = input('Enter a number :')
    l.append(int(x))
    
print('\n')
print('Multiplication of entered numbers in the list is {}'.format(reduce(lambda x , y : x*y , l)))
    
    

