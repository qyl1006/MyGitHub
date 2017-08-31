a = {'a': ['1','2','3'],
	'b': ['4','5'],
	'c': ['6'],
}
love = ['a','b']
for a1,a2 in a.items():
	#print(a1)
	if a1 in love:
		print('我的朋友' + a1 +'喜欢的地方为：' )
		for a11 in a2:
			print('\t' + a11)
  

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
		'abc': '123',
		},
	
	}

for username, user_info in users.items():
	print('\nUsername: ' + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	#location = user_info['location']
	
	print('\tFull name: ' + full_name.title())
	#print('\tLocation: ' + location.title())
	for a, b in user_info.items():
		if 'first'  != a:
			if 'last' != a:
				print('\t' + a + ':' + b)



a = (1,2,'3','s','h',)
print(len(a))
b = len(a)
print(b)
if b >= 3:
	print('Hello')

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print('\nThe number ' + str())
