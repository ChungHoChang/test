fahrenheit = input('What is the temperature in fahrenheit?')
if not fahrenheit.isnumeric():
    print('Input is not a number.')
    exit()
else:
    celsius = (int(fahrenheit) - 32) * 5/9
    print('Temperature in celsius is ' + str(round(celsius, 2)))
