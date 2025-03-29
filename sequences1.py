def divisors(n):
    return len([1] + [x for x in range(2,n) if n%x==0])
def count(n):
    total = 0
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(2,n):
            if n % i ==0:
                total += 1
    return total+1
    