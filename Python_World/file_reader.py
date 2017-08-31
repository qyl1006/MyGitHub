#读取文件名称存储在变量filename
filename = 'file/user.txt'
#获取时间
import time
interview_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

#定义一个用户输入姓名，然后添加访问记录到文件的while
while True:
	name = input('请输入您的名字:')
	print("(输入'q'退出)")
	if name != 'q':
		#name = input('请输入您的名字:')
		print('您好！' + name)

		with open(filename, 'a') as file_object:
			file_object.write('日记:' + name + '曾访问过，' + '时间:' + interview_time + '\n')
	else:
		break	
