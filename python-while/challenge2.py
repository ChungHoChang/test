import random

lower = 1
upper = 10
ans = random.randint(lower, upper)
guess = 0
count = 0
print(f'Guess a number between {lower} and {upper}:')

while guess != ans:
    count += 1
    guess = input(f'Enter guess #{count} :')

    if guess.isnumeric():
        guess = int(guess)
        if guess > ans:
            print('Your guess is too high, try again!')
        elif guess < ans:
            print('Your guess is too low, try again!')
    else:
        print('Numbers only, please!')

else:
    print(f'You guess it in {count} tryies!')
