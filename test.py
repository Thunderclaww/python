num = int(input('Enter the number of Fibonacci numbers you want: '))
a = 0
b = 1
i = 0

while i < num:
    print (a)
    a, b = b, a+b
    i+=1
