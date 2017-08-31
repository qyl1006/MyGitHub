from user_9_12 import User
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
