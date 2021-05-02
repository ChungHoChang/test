print('Simple calculator!')
is1stTime = True

while is1stTime or input('Do you want to continue?').lower() in ['y', 'yes']:
    no1st = input('First number?')
    if not no1st.isdecimal():
        print('Please input a number.')
        exit()

    arr = [['+', '-', '*', '/', '**', '%'], ['Sum', 'Difference', 'Product', 'Quotient', 'Exponent', 'Modulus']]
    oper = input('Operation?')
    StrOper = None
    if not oper in arr[0]:
        print('Operation not recognized.')
        exit()
    else:
        i = arr[0].index(oper)
        StrOper = arr[1][i]

    no2nd = input('Second number?')
    if not no2nd.isdecimal():
        print('Please input a number.')
        exit()

    result = eval(f'{no1st}{oper}{no2nd}')
    print(f'{StrOper} of {no1st} {oper} {no2nd} equals {result}')
    is1stTime = False
