def city_country(city, country, population=''):
	"""城市与国家"""
	if population:
		c_y = city + ',' + country + '-' + population
	else:
		c_y = city + ',' + country 
		
	return c_y.title()
	
