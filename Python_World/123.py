available_toppings = ['mushrooms','olives','green peppers','pepperoni','pinea[[le','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding ' + requested_topping + '.')
	else:
		print("Sorry,we don't have "+ requested_topping +'.')
print('\nFinished making your pizza!')


current_users = ['admiN','qyuelin','yuelin','qinyuelin','qyl','abc']
new_users = ['Admin','Qyl','zxc','asd','qwe']
 #current_users.lower()
for new_user in new_users:
	if new_user.lower() in current_users:
		print('该用户名已被使用，请重新输入！')
	else:
		print('该用户名未被使用。')
		
		
abc = [1,2,3,4,5,6,7,8,9]
print(abc)

for a in abc:
	print(a)
	if a >3:
		print('th')
	elif a >2:
		print('rd')
	elif a >1:
		print('nd')
	else:
		print('st')
