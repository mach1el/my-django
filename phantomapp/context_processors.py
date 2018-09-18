import random
from phantomapp.models import *

def RandomBlog(request):
	list = []
	blogs = BlogContent.objects.all()
	ids = random.sample(range(1,len(blogs)+1),3)
	for id in ids:
		list.append(BlogContent.objects.get(pk=id))

	return {'random_blogs' : list}


def RandomProduct(request):
	list = []
	products = ShopProduct.objects.all()
	ids = random.sample(range(1,len(products)+1),3)
	for id in ids:
		list.append(ShopProduct.objects.get(pk=id))

	return {'random_products' : list}


def UserInfo(request):
	if request.user.is_authenticated:
		if request.user.username == "admin":
			user_profile = {}
		else:
			user_profile = UserProfile.objects.get(username=request.user.username)
	else:
		user_profile = {}

	return {'user_profile' : user_profile}

def ProductCategory(request):
	books = ShopProduct.objects.filter(category=1)
	laptops = ShopProduct.objects.filter(category=2)
	smartwatch = ShopProduct.objects.filter(category=3)
	network_devices = ShopProduct.objects.filter(category=4)

	return {
		'books' : books,
		'laptops' : laptops,
		'smartwatch' : smartwatch,
		'network_devices' : network_devices,
	}