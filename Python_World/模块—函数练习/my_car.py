"""从一个模块导入多个类"""
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2017)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.get_descriptive_name())


"""导入整个模块，在使用module_name.class_name访问需要的类"""
import car

my_beetle = car.Car('volkswagen', 'beetle', 2017)
print(my_beetle.get_descriptive_name())


my_tesla = car.ElectricCar('tesla', 'roadster', 2017)
print(my_tesla.get_descriptive_name())
