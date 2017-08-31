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
	
class Privileges():
	"""管理员权限的类"""
	def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
		"""初始化管理员权限的属性"""
		self.privileges = privileges
			
	def show_privileges(self):
		"""打印显示管理员的权限"""
		shows = self.privileges
		print('管理员的权限有：')
		for show in shows:
			print(show)
	
                                                                                                       	
class Admin(User):
	"""管理员"""
	def __init__(self, first_name, last_name, age, school):
		"""初始化父类的属性，在初始化privileges的属性"""
		super().__init__(first_name, last_name, age, school)
		self.privileges = Privileges()
		                                                                                       
	#def show_privileges(self): 
		#"""打印显示管理员的权限"""
		#shows = self.privileges
		#print('管理员的权限有：')
		#for show in shows:
			#print(show)
			
Admin = Admin('秦', '桧', '22', '斯巴达')
Admin.privileges.show_privileges()

if callable(Admin('秦', '桧', '22', '斯巴达')):
	print('True')
