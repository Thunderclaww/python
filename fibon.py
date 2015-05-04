def fib(n):
    a,b,i= 0,1,0
    while i < n:
        print(a, end=" ")
        a,b = b, a+b
        i+=1

fib(20)
