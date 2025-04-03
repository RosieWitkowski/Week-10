import random

print("Hello, world!")
print("Change 1.")


x = random.randint(1, 50)
guess = int(input("Guess: "))

if x == guess:
    print("Win! ヽ(°‿ °*ヽ)ヽ۹ ⌤_⌤ ۹")
else:
    print("Lose. ಠ⌣ಠ") 
