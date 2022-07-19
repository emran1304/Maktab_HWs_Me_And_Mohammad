def celsius_to_fahrenheit(t):
    return t*1.8 + 32


print(celsius_to_fahrenheit(10))

celsius = [10 , 15 , 20 , 40 , 60]
fahrenheit = list(map(celsius_to_fahrenheit , celsius))

print(fahrenheit)