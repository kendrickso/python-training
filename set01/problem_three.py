def roman_numeral(text):
	roman_decimal = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	sum = 0
	curr = 0
	prev = 0
	
	for x in range(len(text)-1,-1,-1):
		curr = roman_decimal[text[x]]
		if curr >= prev:
			sum += curr
		else:
			sum -= curr
		prev = curr
	
	return sum


print roman_numeral("XIV")
print roman_numeral("CCC")
