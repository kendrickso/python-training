int_list = [2, 5, 4]
sq = lambda x: x*x
perfect_squares = (sq(x) for x in int_list)

for x in perfect_squares:
	print x
