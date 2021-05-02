import random

lower = 1
upper = 5
ans = random.randint(lower, upper)
guess = 0
count = 0

while ans != guess:
    count += 1
    guess = input(f'Guess a number between {lower} and {upper}:')

    if guess.isnumeric():
        guess = int(guess)

else:
    print(f'You guess it in {count} tryies!')
