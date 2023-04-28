"""Считаем время выполнения функции или алгоритма"""
import time


time_start = time.time()


time_finish = time.time()
time_span = time_finish - time_start

print(time_span, 'seconds')

# # visitors - массив номеров пассажиров.
# # Каждый пассажир проехал столько раз, сколько раз встречается его номер
# def checkviz():
# 	visitors = [0,2,3,2,0,4,1,1,2]
# 	entries_by_visitor = [0] * 5
# 	best_visitor = 0
#
# 	for visitor in visitors:
# 		entries_by_visitor[visitor] += 1
# 		if entries_by_visitor[visitor] > entries_by_visitor[best_visitor]:
# 			best_visitor = visitor
#
# 	print(best_visitor)
#
# checkviz()