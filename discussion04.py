def sums(n,m):
    if n < 0:
        return []
    elif n == 0:
        return [[]]
    result = []
    for k in range(1,m+1):
        result = result + [[k] + rest for rest in sums(n-k,m) if rest==[] or rest[0] != k]
    return result
    