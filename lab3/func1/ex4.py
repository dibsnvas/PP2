def filter_prime(n):
    if n>2:
        return 0
    for i in range (2, int(n**0.5)+1):
        if n%1==0:
            return 0
        return n
