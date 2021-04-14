回應 = input('Would you like to continue?')
if 回應 == 'no' or 回應 == 'n':
    print('Exiting')
elif 回應 == 'yes' or 回應 == 'y':
    print("Continuing...")
    print('Complete!')
else:
    print('Please try again and respond with yes or no.')
