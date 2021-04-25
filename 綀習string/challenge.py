first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'


fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'


# First challenge
print(' '*7 + first_value.lower().strip().capitalize())
# Second challenge
print(second_value.replace('-', '').strip().capitalize())
# Third challenge
print(' '*15 + third_value.replace(' ', '').replace('-', ' ').lower().capitalize())
# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!\n')
# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}\n')
