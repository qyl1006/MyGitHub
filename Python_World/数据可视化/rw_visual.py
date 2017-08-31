#导入模块pyplot，并给它指定别名plt
import matplotlib.pyplot as plt
#import matplotlib as mpl
#zhfont = mpl.font_manager.FontProperties(fname='/etc/msyh.ttf')

from random_walk import RandomWalk

#创建一个RandomWalk实例，并将其包含的点都绘制出来

#while True:
	#linewidth = 5000
	#rw = RandomWalk(linewidth)
	#rw.fill_walk()
	
	#point_numbers = list(range(rw.num_points))
	#plt.plot(rw.x_values, rw.y_values)

	## 突出起点与终点
	#plt.scatter(0,0, c='green', edgecolor='none', s=50)
	#plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
				#edgecolor='none', s=50)
	
	## 隐藏坐标轴
	#plt.axes().get_xaxis().set_visible(False)
	#plt.axes().get_yaxis().set_visible(False)
	
	##设置每个坐标轴的取值范围
	##plt.axis([-100, 500, -300, 50])
	
	##设置绘图窗口的尺寸
	##plt.figure(dpi=128, figsize=(10, 6))

	#plt.show()

	#keep_running = input('Make another walk? (y/n): ')
	#if keep_running == 'n':
		#break



#对结果进行可视化
import pygal

linewidth = 5000
rw = RandomWalk(linewidth)
rw.fill_walk()
hist = pygal.Bar()
hist.title = "随机漫步5000点"
##hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
				 ##'12', '13', '14', '15', '16']
hist.x_labels = rw.x_values
#hist.x_title = 'X'
#hist.y_title = "出现总次数"

hist.add('x-y',rw.y_values)
hist.render_to_file('die_visual.svg')
