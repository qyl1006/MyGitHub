print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input('\nFirst number: ')
	if not first_number:
		print('请输入正确的数')
		
	if first_number == 'q':
		break
	second_number = input('\nSecond_number: ')
	if second_number == 'q':
		break
	
	try:
		answer = int(first_number) + int(second_number)
	#except ZeroDivisionError:
		#print("You can't divide by 0!")
	#except ValueError:
		#print('您好！请输入整数。')
	except TypeError:
		print('文本')
	else:
		print(answer)
