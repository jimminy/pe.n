#For all Fibonacci numbers less than n find the sum of all even-valued terms

def fib(fib_seq):
    num = len(fib_seq)
    if(num==0 or num==1):
        return 1
    else:
        return fib_seq[-1]+fib_seq[-2]

seq = []
x = 0
while(x<4000000):
    seq.append(fib(seq))
    x = seq[-1]
    print x