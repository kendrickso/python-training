def matrix(n):
	return [[[str(z)+'-'+str(y)+'-'+str(x) for x in range(n)] for y in range(n)] for z in range(n)]

output = matrix(5)
print output[0][1][3]
