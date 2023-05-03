# def factorize():
# 	k = n
# 	stek = []
# 	for i in range(2, k + 1):
# 		while n % i == 0:
# 			n = n / i
# 			stek.append(i)
# 		if n == 1:
# 			return stek
# 		if i * i >= k and len(stek) == 0:
# 			stek.append(k)
# 			return stek
# 		if i * i >= k and len(stek) == 1:
# 			stek.append(int(k / stek[0]))
# 			return stek
#
#
# result = factorize(int(input()))
# print(" ".join(map(str, result)))


def factorize(n):
    k = int(n**(0.5))
    stek = []
    for i in range(2, k+1):
        print(i)
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
