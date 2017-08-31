class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性restaurant_name和cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def set_number_served(self, number):
		"""设置指定的就餐过额人数"""
		if number >= 0:
			self.number_served = number
		else:
			print('人数不能为负数')
			
	def increment_number_served(self, several):
		"""将就餐的人数增加到指定的人数"""
		if several >= 0:
			self.number_served += several
		else:
			print('人数的增加不能为负数')
	
	def describe_restaurant(self):
		"""打印出该餐馆的名字与美食类型"""
		print('这家餐馆的名字为：' + self.restaurant_name + '，' + '特色菜是：' + 
				self.cuisine_type + '。')
				
	def open_restaurant(self):
		"""打印一条信息显示餐馆正在营业"""
		print(self.restaurant_name + '正在营业。')
		
class IceCreamStand(Restaurant):
	"""冰激凌小店的日常"""
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化父类的属性"""
		"""在初始化冰激凌的属性"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['酸甜', '草莓味', '芒果味','西瓜味']
		
	def display(self):
		"""显示各种冰激凌"""
		displays = self.flavors
		#return displays
		#printprint('冰激凌的口味有：')
		print('冰激凌的口味有：')
		for a in displays:
			print(a)

		
IceCreamStands = IceCreamStand('ABC', '123')
IceCreamStands.flavors.append('柠檬味')
IceCreamStands.display()
#print('冰激凌的口味有：')
#for a in displays:
	#print(a)


