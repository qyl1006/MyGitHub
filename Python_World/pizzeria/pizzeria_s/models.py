from django.db import models

# Create your models here.

class Pizza(models.Model):
	"""披萨店披萨名字类型"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Topping(models.Model):
	"""披萨店的具体配料"""
	Pizza = models.ForeignKey(Pizza)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text[:50] + '...'
