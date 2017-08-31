from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, langage in favorite_languages.items():
	print(name.title() + "'s favorite langage is " + 
		  langage.title() + '.')

from random import randint

class Die():
	"""简单模拟掷骰子游戏"""
	def __init__(self, frquency, sides=6):
		"""初始化骰子的属性"""
		self.sides = sides
		self.frquency = frquency
		
	def roll_die(self):
		"""掷骰子，并打印出随机出现的点数"""
		print('\n掷一颗' + str(self.sides) + '面的骰子' + str(self.frquency) + 
			   '次，出现的点数为：' )
		while True:
			X = randint(1,self.sides)
			print(X)
			Y = self.frquency-1
			self.frquency = Y
			if Y ==0:
				break
			
roll = Die(10,6)
roll.roll_die()

roll = Die(10,10)
roll.roll_die()

roll = Die(10,20)
roll.roll_die()
