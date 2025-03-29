def count_partition(m,n):
    if m == 0:
        return 1
    if m < 0:
        return 0
    if n == 0:
        return 0
    else:
        with_m = count_partition(m-n,n)
        without_m = count_partition(m,n-1)
        return with_m + without_m
