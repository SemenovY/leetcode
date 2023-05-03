def factorize(n):
    k = int(n**(0.5))
    stek = []
    for i in range(2, k+1):
        while n % i == 0:
            n = n / i
            stek.append(i)
        if n == 1:
            return stek
    if n > 1:
        stek.append(int(n))
        return stek

result = factorize(int(input()))
print(" ".join(map(str, result)))
