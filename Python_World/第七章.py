####while True:
	####age = input('请先输入您的年龄： ')
	#####abc = True
	#####while abc:
	####age = int(age)
	####if age < 3:
		####print('您不需要买票免费')
			#####abc = False
	####elif age <= 12:
		####print('您的电影票价格为：10元')
		#####abc =False
	####else:
		####print('您的电影票价格为：15元')
		#####abc = False
	####print('\n')
	
####首先，创建一个待验证用户列表
#### 和一个用于存储已验证用户的空列表
###unconfirmed_users = ['alice','brian','candace']
###confirmed_users = []

####验证每个用户，直到没有未验证用户为止
#### 将每个验证的列表都移到已验证用户列表中
###while unconfirmed_users:
	###current_user = unconfirmed_users.pop()
	
	###print('Verifying user: ' + current_user.title())
	###confirmed_users.append(current_user)
	
####显示所有已验证的用户
###print('\nThe following users have been confirmed:')
###for confirmed in confirmed_users:
	###print(confirmed.title())	
	
###pets = ['dog','cat','dog','goldfish','cat','rabbit','cat','dog']
###print(pets)
###while 'cat' in pets:
	####print(pets)
	###pets.remove('cat')
	####pets.remove('dog')
###while 'dog' in pets:
	###pets.remove('dog')
###print(pets)

###print('\n')
###responses = {}

####设置一个标志，指出调查是否继续
###polling_active = True

###while polling_active:
	####提示输入被调查者的名字和回答
	###name = input('\nWhat is your name? ')
	###response = input('Which mountain would you like to climb someday? ')
	
	####将答案存储在字典中
	###responses[name] = response
	
	####看看是否还有人要参加调查
	###repeat = input('Would you like to let another person respond?(yes/no) ')
	###if repeat == 'no':
		###polling_active = False
		
####调查结束，显示结果
###print('\n---- Poll Results ----')
###print(responses)
###for name, response in responses.items():
	###print(name + ' would like to climb ' + response + '.')

##sandwich_orders = ['a','b','c','pastrami','pastrami','pastrami','pastrami','pastrami']
##finished_sandwiches = []

##while sandwich_orders:
	##if 'pastrami' in sandwich_orders:
		##sandwich_orders.remove('pastrami')
		##continue
		
	##for A in sandwich_orders:
		##print('I made your ' + A + ' sandwich.')
		##sandwich_orders.remove(A)
		##finished_sandwiches.append(A)
	
##print('所有三明治已经制作完成：')
##for B in finished_sandwiches:
	##print(B)


##sandwich_orders = ['a','b','c','pastrami','pastrami','pastrami','pastrami','pastrami']
##print('本店的五香烟熏牛肉已卖完了。')

##while 'pastrami' in sandwich_orders:
	##sandwich_orders.remove('pastrami')
	
##print(sandwich_orders)

##def display_message(username):
	##print('\n' + username + '在本章节学会实参与形参的区别。')
##display_message('qyl')

##def favorite_book(title):
	##print('One of me favorite books is ' + title + '.')

##favorite_book('Alice in Wonderland')


##def describe_pet(pet_name, animal_type = 'dog'):
	##"""显示宠物信息"""
	##print('\nI have a ' + animal_type + '.')
	##print('My ' + animal_type + "'s name is " + pet_name.title() + '.' )
	
##describe_pet(pet_name = 'willie', animal_type = 'abc')
##describe_pet(animal_type = 'abc', pet_name = 'willie' )
##describe_pet('willie' , 'dog')

##def make_shirt(a , b = 'I love Python'):
	###a = input('请输入T恤的尺寸： ')
	###b = input('请输入印在T恤上的字样： ')
	##print('你定制的T恤尺寸为：' + a + '，T恤字样是：' + b +'。')
##make_shirt('中号')

##def describe_city(city , country = '中国'):
	##print(city + '这座城市属于' + country + '。')

##describe_city('北京')
##describe_city(city = '上海')
##describe_city('纽约','美国' )
##describe_city(city = '华盛顿', country = '美国' )



###print(describe_city())
##def someFunction():
   ##pass
	
##print(someFunction())

##def get_formatted_name(first_name, last_name, middle_name = ''):
	##if middle_name:
		##full_name = first_name + ' ' + middle_name + ' ' + last_name 
	##else:
		##full_name = first_name + ' ' + last_name
	##return full_name.title()
	
###musician = get_formatted_name('jimi', 'hendrix')
###print(musician)

###musician = get_formatted_name('john', 'hooker', 'lee')
###print(musician)

###def build_person(first_name, last_name, age = ''):
	###person = {'first': first_name, 'last': last_name}
	###if age:
		###person['age'] = age
	###return person
	
###musician = build_person('jimi', 'hendrix', '27')
###print(musician)


###def get_formatted_name(first_name, last_name):
	###full_name = first_name + ' ' + last_name
	###return full_name.title()
	
##while True:
	##print('\nPlease tell me your name:')
	##f_name = input('First name: ')
	##l_name = input('last name: ')
	##m_name = input('middle_name(回车取消): ')
	##formatted_name = get_formatted_name(f_name, l_name, m_name)
	##print('\nHello, ' + formatted_name + '!')
	##break


##def city_country(city, country):
	##abc = ('"' + city + '，' + country + '"')
	##return abc
##while True:	
	##a_city = input('请输入城市： ')
	##b_country = input('请输入国家： ')
	##musician = city_country(a_city, b_country)
	##print(musician)
	##c = input('(输入’q‘退出)')
	##if c == 'q':
		##break
		
	
#def make_album(singer, album, songs = ''):
	#make_album = {'singer': singer , 'album': album }
	#if songs:
		#make_album['songs'] = songs
	#return make_album

#while True:
	#print("\n(输入'q'退出)")
	
	#a_singer = input('请输入歌手名字：')
	#if a_singer == 'q':
		#break
		
	#b_album = input('请输入专辑名：')
	#if b_album == 'q':
		#break
		
	#c_songs = input('请输入专辑里的歌曲数量：')
	#if c_songs == 'q':
		#break
		
	#musician = make_album(a_singer, b_album, c_songs)
	#print(musician)
	
	
#def print_models(unprinted_designs, completed_models):
	#"""
	#模拟打印每个设计，直到没有未打印的设计为止
	#打印每个设计后，都将其移到completed_models中
	#"""
	#while unprinted_designs:
		#current_desing = unprinted_designs.pop()
		
		##模拟根据设计制作3D打印模型的过程
		#print('Printing model: ' + current_desing)
		#completed_models.append(current_desing)
	##print('\nThe following models have been printed:')
	##for completed_model in completed_models:
		##abc = completed_model
	#return completed_models

#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#completed_models = []

#completed_models = print_models(unprinted_designs[:], completed_models)
#print('\nThe following models have been printed:')
#for completed_model in completed_models:
	#print(completed_model)
	
#print(unprinted_designs)



		
		
##def show_completed_models(completed_models):
	##"""显示打印好的所有模型"""
	##print('\nThe following models have been printed:')
	##for completed_model in completed_models:
		##print(completed_model)
		
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#completed_models = []

##print_models(unprinted_designs, completed_models)
##show_completed_models(completed_models)

##def show_magicians(magicians):
	##print('每个魔术师的名字是：')
	##for magician in magicians:
		##print(magician)
		
##magicians = ['a', 'b', 'c','d']
##show_magicians(magicians)


#def make_great(magicians, modify_magicians):
	#while magicians:
		#current_magician = magicians.pop()
		#modify_magicians.append('the Great ' + current_magician)
	#return modify_magicians
	
#def show_magicians(modify_magicians):
	#print('每个魔术师的名字是：')
	#for magician in modify_magicians:
		#print(magician)
		##a = magician
	##return a

#magicians = ['a', 'b', 'c','d']
#print(magicians)
#modify_magicians = []

#abc = make_great(magicians, modify_magicians)
#show_magicians(modify_magicians)

#print(abc)


#def make_pizza(size, *toppings):
	#"""概述要制作的披萨"""
	#print('\nMakeing a ' + str(size) +
		  #'-inch pizza with the following toppings:')
	#for topping in toppings:
		#print('- ' + topping)

#make_pizza(16, 'pepperoni')
#make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['姓'] = first
	profile['名'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('秦', '跃林', 出生日= '10-06',
								故乡 = '桂林', 现居地 = '南宁')

print(user_profile)

def make_sandwich(*toppings):
	"""概述顾客点的三明治"""
	print("Your point of sandwich contains ingredients: ")
	for topping in toppings:
		print('- ' + topping)
		
#toppings = []
#while True:
	#print('\n(请输入‘q’退出)')
	#topping = input('请输入你需要的配料：')
	#if topping == 'q':
		#break
	#toppings.append(topping)
	
#print(toppings)
make_sandwich('a', 'x', 'z')

def make_car(manufacturer, model, **car_information):
	"""创建一个空字典，里面包含关于汽车的一切信息"""
	cars = {}
	cars['manufacturer'] = manufacturer
	cars['model'] = model
	for key, value in car_information.items():
		cars[key] = value
	return cars
	
car = make_car('上汽通用五菱', '宝骏630', 
				颜色 = '亮黑', 车长 = '2.5m',
				车宽 = '1.2m')
print('\n')
print(car) 
