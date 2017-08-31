def make_pizza(size, *toppings):
	"""概述要制作的披萨"""
	print('\nMakeing a ' + str(size) +
		  '-inch pizza with the following toppings:')
	for topping in toppings:
		print('- ' + topping)
	return toppings
	
