"""定义pizzeria_s的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
	# 主页
	url(r'^$', views.index, name='index'),
	
	# 显示所有的批萨
	url(r'^pizzas/$', views.pizzas, name='pizzas'),
	
	# 特定主题的批萨配料页面
	url(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
]
