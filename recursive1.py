def split(n):
    return n // 10 , n % 10
def sum_digits(n):
    if n < 10 :
        return n
    else :
        all_but_last , last = split(n)
        return sum_digits(all_but_last) + last
def luhn_sum(n):
    if n < 10 :
        return n
    else :
        all_but_last , last = split(n)
        return luhn_sum_double(all_but_last) + last
def luhn_sum_double(n):
    all_but_last , last = split(n)
    luhn_digits = sum_digits(last * 2)
    if n < 10:
        return luhn_digits
    else :
        return luhn_digits + luhn_sum(all_but_last)