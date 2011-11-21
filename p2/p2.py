#For all Fibonacci numbers less than n find the sum of all even-valued terms

def fib(seq):
    num = len(seq)
    if(num==0 or num==1):
        return 1
    else:
        return seq[-1]+seq[-2]

def fib_lt(max, x = 0, seq = []):
    while(x<n):
        seq.append(fib(seq))
        x = seq[-1]
    return seq[:-1]

n = 4000000
print fib_lt(n)

