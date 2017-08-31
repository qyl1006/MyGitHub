#导入模块pyplot，并给它指定别名plt
import matplotlib.pyplot as plt
import matplotlib as mpl
zhfont = mpl.font_manager.FontProperties(fname='/etc/msyh.ttf')

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=5)

#设置图表标题并给坐标轴加上标签
plt.title('立方表', fontproperties=zhfont, fontsize=24)
plt.xlabel('整数', fontproperties=zhfont, fontsize=15)
plt.ylabel('立方值', fontproperties=zhfont, fontsize=15)

#设置刻度标记的大少
plt.tick_params(axis='both', which='major', labelsize=14)       

#设置每个坐标轴的取值范围
plt.axis([0, 5500, 0, 150000000])

plt.show()
