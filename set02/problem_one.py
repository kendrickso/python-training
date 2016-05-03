def pyramid(height):
	ones = ''
	for x in xrange(height):
		spaces = ''
		ones += '1 '
		for y in xrange(height - x):
			spaces += ' '
		yield spaces + ones.rstrip()

for x in pyramid(5):
	print x
