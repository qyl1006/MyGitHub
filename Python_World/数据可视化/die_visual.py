from die import Die

import pygal
# 创建一个D6
die_1 = Die(8)
die_2 = Die(8)
die_3 = Die(10)


#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
	
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)
	
# 分析结果
frequencies = []
x_ = []
max_result = die_1.num_sides + die_2.num_sides +die_3.num_sides
for value in range(3, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)   #个点数出现的总次数的list
	x_.append(value)
	
#for i in results:
	#if not i in x_labels:
		#x_labels.append(i)
#for value in x_labels:
	#frequency = results.count(value)
	#frequencies.append(frequency)


#对结果进行可视化
#hist = pygal.Bar()

#hist.title = "掷两颗6面骰子1000000次"
###hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
				 ###'12', '13', '14', '15', '16']
#hist.x_labels = x_
#hist.x_title = '相乘点数'
#hist.y_title = "出现总次数"

#hist.add('D6+D6', frequencies)
#hist.render_to_file('die_visual.svg')

###对结果可视化
import matplotlib.pyplot as plt
import matplotlib as mpl
zhfont = mpl.font_manager.FontProperties(fname='/etc/msyh.ttf')

x_values = x_
y_values = frequencies

plt.scatter(x_values, y_values, c='red',
				edgecolor='none', s=10)

#设置图表标题并给坐标轴加上标签
plt.title('掷两颗6面骰子10000次', fontproperties=zhfont, fontsize=24)
plt.xlabel('点数', fontproperties=zhfont, fontsize=24)
plt.ylabel('出现总次数', fontproperties=zhfont, fontsize=15)

#设置每个坐标的取值范围


#设置刻度标记的大少
plt.tick_params(axis='both', which='major',labelsize=14)

plt.show()


	
