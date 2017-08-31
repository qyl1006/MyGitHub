from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
	"""披萨店的主页"""
	return render(request, 'pizzeria_s/index.html')
	
def pizzas(request):
	"""显示所有的主题"""
	pizzas = Pizza.objects.order_by('date_added')
	context = {'pizzas': pizzas}
	return render (request, 'pizzeria_s/pizzas.html', context)
	
def pizza(request, pizza_id):
	"""显示每个批萨及其配料组成"""
	pizza = Pizza.objects.get(id=pizza_id)
	entries = pizza.topping_set.order_by('-date_added')
	context = {'pizza': pizza, 'entries': entries}
	return render(request, 'pizzeria_s/pizza.html', context)
