import math as maths

print("Hello, world!")
print("Change 1.")

x = maths.random(1, 50)
guess = int("Guess: ")

if x == guess:
    print("Win!")
else:
    print("Lose.") 