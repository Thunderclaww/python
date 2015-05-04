import math

denom = [0.25,0.1,0.05,0.01]

def change(amount):
    q = math.floor(amount/denom[0])
    amount = amount - q*denom[0]
    d = math.floor(amount/denom[1])
    amount = amount - d*denom[1]
    n = math.floor(amount/denom[2])
    amount = amount - n*denom[2]
    p = math.floor(amount/denom[3])
    amount = amount - p*denom[3]

    print("You need: \n",
          q, " quarters, \n",
          d, " dimes, \n",
          n, " nickels, \n",
          p, " pennies.")

change(float(input("Enter the change needed: ")))
