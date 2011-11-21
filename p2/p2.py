#For all Fibonacci numbers less than n find the sum of all even-valued terms

def fib(n):
    if(n==0 or n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

i = 0
x = 0
while(x<4000000):
    x = fib(i)
    i = i+1
    print x