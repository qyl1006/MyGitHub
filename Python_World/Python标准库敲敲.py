def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
	
median = fact(1000)	
print(median)

