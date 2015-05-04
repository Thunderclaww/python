import random
import time

num = int(input("Guess a number: "))
actual = random.randint(1,100)

while num != actual:
    if num > actual:
        print("Lower")
    else:
        print("Higher")
    num = int(input("Guess another number: "))

print("You got it! The answer was", actual)
time.sleep(4)
