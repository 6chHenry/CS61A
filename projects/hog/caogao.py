def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    k = 2
    t = 0
    while k < n:
        if n % k == 0:
            t += 1
        k += 1
    print(t)
num_factors(25)
