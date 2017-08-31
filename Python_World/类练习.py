class Dog():
	"""一次模拟小狗的简单尝试"""
	
	def __init__(self, name, age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + ' is now sitting.')
		
	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + ' rolled over!')
		
		
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + ' years ild.')
my_dog.sit()
my_dog.roll_over()

print("My dog's name is " + your_dog.name.title() + '.')


class Restaurant():
	
	def __init__(self, restaurant_name, cuisine_type):
		"""初始化属性restaurant_name和cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		"""打印出该餐馆的名字与美食类型"""
		print('这家餐馆的名字为：' + self.restaurant_name + '，' + '特色菜是：' + 
				self.cuisine_type + '。')
				
	def open_restaurant(self):
		"""打印一条信息显示餐馆正在营业"""
		print(self.restaurant_name + '正在营业。')
		
restaurant = Restaurant('甘家界柠檬鸭', '柠檬鸭')
print(restaurant.restaurant_name)
print('特色菜：' + restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

class User():
	"""创建一个用户user的类"""
	def __init__(self, first_name, last_name, age, school):
		
		"""初始化属性参数"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.school = school
	
	def describe_user(self):
		"""打印用户信息摘要"""
		print('姓名：' + self.first_name + self.last_name + ' 年龄：' + str(self.age) +
				' 学校：' + self.school)
				
	def greet_user(self):
		print('Hello! ' + self.first_name + self.last_name + '，你今年' + 
				str(self.age) + '岁，' + '可结婚了没有？')

user = User('秦', '岳林', '25', '加利登大学')

user.describe_user()
user.greet_user()


class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self, make, model, year, ):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 30
		
	def update_odometer(self, mileage):
		"""将里程表读数设置为指定的值"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	
	def increment_odometer(self, miles):
		"""将里程表读数增加指定的量"""
		self.odometer_reading += miles
		
	def get_descriptive_name(self):
		"""返回简洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_obometer(self):
		"""打印一条指出汽车里程的消息"""
		print('This car has  ' + str(self.odometer_reading) + ' miles on it.')
		
	def increment_odometer(self, miles):
		"""将里程表读数增加指定的量"""
		if miles >=0:
			self.odometer_reading += miles
		else:
			print('里程表增加量不能为负数')
		print('ABC This car has  ' + str(self.odometer_reading) + ' miles on it.')
my_new_car = Car('audi', 'a4', '2017')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 100
my_new_car.odometer_reading = 23
my_new_car.read_obometer()

my_new_car.increment_odometer(100)
my_new_car.read_obometer()

class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	def __init__(self, battery_size = 70):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print('This car has a ' + str(self.battery_size) + '-KWH battery.')
	
	def upgrade_battery(self, ):
		"""检查电瓶容量，并对它进行升级"""
		if self.battery_size != 85:
			battery_size = 85
			self.battery_size = battery_size
		print(str(self.battery_size))
		
	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程"""
		if self.battery_size == 70:
			range =  240
		elif self.battery_size == 85:
			range = 280
		
		message = "This car can go approximately " + str(range)
		message += ' miles on a full charge.'
		print(message)

	def upgrade_battery(self):
		"""检查电瓶容量，并对它进行升级"""
		if self.battery_size != 85:
			battery_size = 85
			self.battery_size = battery_size
class ElectricCar(Car):
	"""电动汽车的独特之处"""
	
	def __init__(self, make, model, year):
		"""初始化父类的属性"""
		super().__init__(make, model, year)
		self.battery = Battery()
							
my_tesla = ElectricCar('tesla', 'model s', 2017)
print(my_tesla.get_descriptive_name())

#my_tesla.battery_1.battery_size = 11

my_tesla.battery.upgrade_battery()

my_tesla.battery.get_range()
