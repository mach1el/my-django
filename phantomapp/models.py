from django.db import models
from django.contrib.auth.models import User

class BlogLabel(models.Model):
	name = models.CharField(max_length=255,unique=True)

	def __str__(self):
		return self.name

class BlogContent(models.Model):
	label = models.ForeignKey(BlogLabel,on_delete=models.PROTECT)
	title = models.CharField(max_length=255,unique=True)
	intro = models.TextField()
	author = models.CharField(max_length=255)
	content = models.TextField()
	datetime = models.DateTimeField(auto_now_add=True,blank=True)
	image = models.ImageField(upload_to="blog_images/")

	def __str__(self):
		return self.title

class ShopCategory(models.Model):
	name = models.CharField(max_length=255,unique=True)

	def __str__(self):
		return self.name

class ShopProduct(models.Model):
	category = models.ForeignKey(ShopCategory,on_delete=models.PROTECT)
	name = models.CharField(max_length=255,unique=True)
	price = models.IntegerField()
	description = models.TextField()
	ordered_times = models.IntegerField()
	image = models.ImageField(upload_to="shop_products/")

	def __str__(self):
		return self.name

class Contact(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	subject = models.CharField(max_length=255)
	message = models.TextField()

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	class Meta:
		db_table = u'Contact'

class UserProfile(models.Model):
	username = models.CharField(max_length=255,unique=True)
	company = models.CharField(max_length=255,blank=True)
	country = models.CharField(max_length=255,blank=True)
	state = models.CharField(max_length=255,blank=True)
	address = models.CharField(max_length=255,blank=True)
	telephone = models.CharField(max_length=255,blank=True)

	def __str__(self):
		return self.username

class Order(models.Model):
	username =  models.CharField(max_length=255,blank=True)
	email = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	telephone = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return 'Order{}'.format(self.id)

	def get_total_cost(self):
		return sum(product.get_cost() for product in self.products.all())

class OrderProduct(models.Model):
	purchase = models.ForeignKey(Order,related_name="products",on_delete=models.PROTECT)
	product = models.ForeignKey(ShopProduct,related_name="products",on_delete=models.PROTECT)
	price = models.IntegerField()

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price