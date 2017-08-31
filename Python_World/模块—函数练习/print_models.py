#def print_models(unprinted_designs, completed_models):
	#"""
	#模拟打印每个设计，直到没有未打印的设计为止
	#打印每个设计后，都将其移到completed_models中
	#"""
	#while unprinted_designs:
		#current_desing = unprinted_designs.pop()
		
		##模拟根据设计制作3D打印模型的过程
		#print('Printing model: ' + current_desing)
		#completed_models.append(current_desing)

#def show_completed_models(completed_models):
	#"""显示打印好的所有模型"""
	#print('\nThe following models have been printed:')
	#for completed_model in completed_models:
		#print(completed_model)
		
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#completed_models = []

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm 
#from printing_functions import print_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#show_completed_models(completed_models)
pm(unprinted_designs, completed_models)
scm(completed_models)
