import math

num = int(input("Enter the number of decimal places you want Pi to: "))
i = 0

while int(i) < num:
    print(str(math.pi)[i+2])
    i += 1
