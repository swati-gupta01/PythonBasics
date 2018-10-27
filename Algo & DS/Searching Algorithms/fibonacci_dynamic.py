def fib(n):
    seq=[0]*n
    seq[0]=0
    seq[1]=1
    for i in range(2,n):
        seq[i]=seq[i-1]+seq[i-2]
    print(seq)
    return seq[n-1]

print(fib(9))