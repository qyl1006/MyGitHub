#导入模块pyplot，并给它指定别名plt
import matplotlib.pyplot as plt
import matplotlib as mpl
zhfont = mpl.font_manager.FontProperties(fname='/etc/msyh.ttf')



#input_values = [1,2,3,4,5]
#squares = [1,4,9,16,25]
#plt.plot(input_values, squares, linewidth=5)

##设置图表标题，并给坐标轴加上标签
#plt.title('Square Numbers', fontsize=24)
#plt.xlabel('Value', fontsize=15)
#plt.ylabel('Square of Value', fontsize=15)

## 设置刻度标记的大少
#plt.tick_params(axis='both', which='major', labelsize=15)
#plt.scatter(2,1,)
#plt.show()

#plt.scatter(x_values, y_values, edgecolor='none',)

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=5)

#设置图表标题，并给坐标轴加上标签
plt.title('中国', fontproperties=zhfont, fontsize=24)
plt.xlabel('年代', fontproperties=zhfont, fontsize=15)
plt.ylabel('人口', fontproperties=zhfont, fontsize=15)

# 设置刻度标记的大少
plt.tick_params(axis='both', which='major', labelsize=10)

#
plt.axis([0, 1100, 0, 1100000])
plt.savefig('/home/qyl/桌面/002.png', bbox_inches='tight')
