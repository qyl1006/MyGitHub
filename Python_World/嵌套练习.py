aliens = []

for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
	

print('Total number of aliens: ' + str(len(aliens)) )

		

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	

for alien in aliens[:5]:
	print(alien)
print('...')


for alien in aliens[0:5]:
	if alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
	elif alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
		
for alien in aliens[:7]:
	print(alien)
print('\n' + '...')

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms','extra cheese'],
	}
	
print('Your ordered a ' + pizza['crust'] + '-crust pizza ' +
	'with the following toppings:')
	
for topping in pizza['toppings']:
	print('\n' + topping)
	
print(pizza['toppings'])

favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell'],
	}
for name,languages in favorite_languages.items():
	if len(languages) == '1':
		print('\n' + name.title() + "'s favorite languages is " + languages)
	else:
		print('\n' + name.title() + "'s favorite languages are:")
		for language in languages:
			print('\n' + language.title())
			
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		'birthday': '10-06', 
		},
	}
	
for username, user_info in users.items():
	print('\nUsername: ' + username)
	print(str(len(user_info)))
	if len(user_info) < 4:
		full_name = user_info['first'] + ' ' + user_info['last']
		location = user_info['location']
	
		print('\tFull name: ' + full_name.title())
		print('\tLocation: ' + location.title())
	else:
		full_name = user_info['first'] + ' ' + user_info['last']
		location = user_info['location']
		birthday = user_info['birthday']
		
		print('\tFull name: ' + full_name.title())
		print('\tLocation: ' + location.title())
		print('\tBirthday: ' + birthday)

print('\n')

ailen_0 = {'colors': 'green','bss': 5}
#ailen_1 = {'color':'red','b': 10}
#people = [ailen_0,ailen_1]

#print(ailen_0['b'])
#print(people)
#for a in people:
	
	#print('\tColor: ' + a['color'])
	#print('\tColor2: ' + a['color'])
	#print('\tPointss: ' + b['pointss'])
for color,bs in a.items():
	print('\tColor2: ' + color)
	print('\tPointss: ' + bs)
