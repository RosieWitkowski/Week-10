import random

print("Hello, world!")
print("Change 1.")


play = True
x = random.randint(1, 25)

while play:
    guess = int(input("Guess: "))

    if x == guess:
        print("Win! ヽ(°‿ °*ヽ)ヽ۹ ⌤_⌤ ۹")
    else:
        print("Lose. ಠ⌣ಠ") 
        if guess > x:
            print("Too big.")
        else:
            print("Too small.")

    options = ['y', 'n']
    choice = 'A'
    while choice not in options:
        choice = input("Continue? Y/N ").lower()[:1]
    
    if choice == 'n':
        play = False