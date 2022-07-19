username = input('Please Enter Username :')
password = input('Please Enter PAssword :')

if (username == 'admin') and (password == 'admin'):
    print('Welcome on Admin')
    
elif (username == 'admin') and (password != 'admin'):
    print('Wrong')
    
else:
    print('Hello {}'.format(username))