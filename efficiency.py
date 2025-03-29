def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-2) + fib(n-1)
def count(f):
    def counted(n):
        counted.call_count +=1
        return f(n)
    counted.call_count = 0
    return counted
def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memorized

s=[2,3]
t=[5,6]
a=s+[t]
b=a[1:]
a[1]=9
b[1][1]=0