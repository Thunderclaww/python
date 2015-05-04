import math
import sys

num = int(input("Enter the number of decimal places you want e to: "))
while num > 15:
    print("Sorry, that number is too large. Please try again.")
    num = int(input("Enter the number of decimal places you want e to: "))
i = 0
output = "2."

while int(i) < num:
    output+=str(math.e)[i+2]
    i += 1
print(output)
