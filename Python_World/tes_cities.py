import unittest
from city_cities import city_country

class NameTestCase(unittest.TestCase):
	"""测试city_country"""
	
	def test_city_country(self):
		""""能够正确处理像Santiago,Chile-population 5000000这样的吗？"""
		c_y = city_country('santiago', 'chile','population 5000000')
		self.assertEqual(c_y, 'Santiago,Chile-Population 5000000')
		
unittest.main()	
