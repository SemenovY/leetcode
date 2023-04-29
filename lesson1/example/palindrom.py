"""Считаем палиндром методом вывода наоборот"""
def palindrom(arr):
	c = []
	for i in range(0, len(arr)):
		a = arr[i]
		b = arr[i][::-1]
		if a == b:
			c.append(arr[i])
	c.sort()
	return c


arr = ['65535']
print(palindrom(arr))
