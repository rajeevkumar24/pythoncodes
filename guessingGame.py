from random import randint

num = randint(0, 100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guesses = [0]
limit = 5

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? " ))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    # compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
    if len(guesses) > limit:
        print('BETTER LUCK NEXT TIME!!')
        break
    # add guess to the list
    guesses.append(guess)

    if guesses[-2]:
        if abs(num-guess) > abs(num - guesses[-2]):
            print('WARMER!')

        else:
            print('COLDER!')

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')




