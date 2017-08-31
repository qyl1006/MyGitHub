alien_0 = {'color':'green','points':5}
print(alien_0['points']**2)

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['x_position'] = 100
alien_0['y_position'] = 125
print('\n')
print(alien_0)

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print('Original x_position: '+str(alien_0['x_position']))
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position']+x_increment
print('New x_position: '+str(alien_0['x_position']))

print(alien_0)
del alien_0['x_position']
print(alien_0)

favorite_languages = {
	'jen':'Python',
	'sarah':'c',
	'edward':'Ruby',
	'phil':'Python',
	'a':'第一个',
	'Z':'最后一个',
}
for name, language in sorted(favorite_languages.items()):
	print(name.title() + " 's favorite languages is " + language.title() + ".")
for name in favorite_languages.keys():
	print(name.title())
print(favorite_languages['sarah'].title())
print('\n')
friends = ['phil','jen']
print(friends)
for name in favorite_languages.keys():	
	if name in friends:
		print('谢谢!' + name + '你已参加了调查。' )
	else:
		print(name + '请参加调查。')
for name in sorted(favorite_languages.keys()):
	print(name)
print('\n' + 'The following languages have been mentioned:')
for language in set(favorite_languages.values()):
	print(language.title())
张小明 = {
	'first_name':'张',
	'last_name':'xiaoming',
	'age':'24',
	'city':'南宁',
	}
print(张小明)

number = {
	'a':'520',
	'b':'521',
	'c':'12306',
	'd':'110',
	'e':'120',
	}
for name in number.keys():
	print(name+ '喜欢的数字是： '+ 'love')
print('a他喜欢的数字是:'+number['a']+'。')
print('b他喜欢的数字是:'+number['b']+'。')
print('c他喜欢的数字是:'+number['c']+'。')
print('d他喜欢的数字是:'+number['d']+'。')
print('e他喜欢的数字是:'+number['e']+'。')


user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
	}
for key, value in user_0.items():
	print('\nKey: '+ key)
	print('Value: '+ value)

river_country = {
	'nile':'egypt',
	'长江':'中国',
	'黄河':'中国',
	}
for river,country in sorted(river_country.items()):
	print('这条' + river + '流经' + country + '.')
for river in sorted(river_country.keys()):
	print('河流名字：' + river)
for country in sorted(river_country.values()):
	print('流经国家为：' + country)
