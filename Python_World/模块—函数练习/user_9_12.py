class User():
	"""创建一个用户user的类"""
	def __init__(self, first_name, last_name, age, school,):
		
		"""初始化属性参数"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.school = school
		self.login_attempts = 0
		
	def increment_login_attempts(self, increase):
		"""将login_attempts值增加1"""
		#increase = 1
		self.login_attempts += 1
		
	def reset_login_attempts(self, reset):
		"""将login_attempts值重置为0"""
		#reset = 0
		self.login_attempts = 0
		
	def display(self):
		print('login_attempts: ' + str(self.login_attempts))
	
