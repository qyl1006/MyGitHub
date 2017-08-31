"""10-4练习题"""

#读取文件名称存储在变量filename
filename = 'file/user.txt'
love = 'file/Like_programming.txt'


while True:
	#获取当前时间
	import time
	interview_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
	
	#用户输入姓名，回答问题，并把访问记录与回答内容分别存储相应文件
	name = input('请输入您的名字:')
	print("(输入'q'退出)")
	if name != 'q':
		love_filename = input('您好！' + name + '，你为什么喜欢编程，可以告诉我吗？ ')
		with open(love, 'a') as file_object:
			file_object.write(name + '喜欢编程的原因是：' + love_filename + '。' + '\n')
		with open(filename, 'a') as file_object:
			file_object.write('日记:' + name + '曾访问过，' + '时间:' + interview_time + '\n')
			
	else:
		break	


#"""10-5练习题"""

#filename = 'file/Like programming.txt'
#print(name)
##while:
	##reason = input('')
