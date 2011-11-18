#Sum of all multiples of factors x,y, and ...z between n and m.
def sum_multiples(factors, n, m):
    j = len(factors)
    result = 0
    while(n<m):
        i = 0
        while(i<j):
            if(n%factors[i]==0):
                result = result + n
                i = j
            i = i + 1
        n = n+1
    return result

F = [3,5]
n = 0
m = 10

print sum_multiples(F, n, m)