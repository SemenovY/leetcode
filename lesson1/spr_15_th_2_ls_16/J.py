"""
Основная теорема арифметики говорит:
любое число раскладывается на произведение простых множителей
единственным образом, с точностью до их перестановки.
Например:
Число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5).
Три варианта отличаются лишь порядком следования множителей.
Разложение числа на простые множители называется факторизацией числа.
Напишите программу, которая производит факторизацию переданного числа.
Формат ввода
В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.
Формат вывода
Выведите в порядке неубывания простые множители,
на которые раскладывается число n.
"""
from typing import List


def factorize(number: int) -> List[int]:
	"""
	Получили на вход число
	через цикл гоняем от 2 до числа
	пока остаток не дробное число делим и добавляем в стек
	как только дробное, сравниваем с 1 и выходим
	либо перебираем числа дальше
	:param number:
	:return:
	"""
	if number == 1:
		return False
	result = []

	for i in range(2, number + 1):
		while number % i == 0:
			number /= i
			result.append(i)

		if number == 1:
			return result







result = factorize(int(input()))
print(" ".join(map(str, result)))

















# # def factorize():
# # 	k = n
# # 	stek = []
# # 	for i in range(2, k + 1):
# # 		while n % i == 0:
# # 			n = n / i
# # 			stek.append(i)
# # 		if n == 1:
# # 			return stek
# # 		if i * i >= k and len(stek) == 0:
# # 			stek.append(k)
# # 			return stek
# # 		if i * i >= k and len(stek) == 1:
# # 			stek.append(int(k / stek[0]))
# # 			return stek
# #
# #
# # result = factorize(int(input()))
# # print(" ".join(map(str, result)))
#
#
# def factorize(n):
#     k = int(n**(0.5))
#     stek = []
#     for i in range(2, k+1):
#         print(i)
#         while n % i == 0:
#             n = n / i
#             stek.append(i)
#         if n == 1:
#             return stek
#     if n > 1:
#         stek.append(int(n))
#         return stek
#
#
# result = factorize(int(input()))
# print(" ".join(map(str, result)))
