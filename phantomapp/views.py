import os,json,datetime,xlsxwriter,feedparser
from cart.cart import Cart
from phantomapp import forms
from phantomapp.models import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.views.decorators.http import require_POST

def error404(request,exception):
	return render(request,"404.html")

def error500(request,*args):
	return render(request,"505.html")

def index(request):
	return render(request,"index.html")

def about(request):
	return render(request,"about.html")

def portfolio(request):
	return render(request,"portfolio.html")

def rss(request):
	feeds = feedparser.parse('https://feeds.feedburner.com/TheHackersNews')
	return render(request,"rss.html",{'feeds':feeds})

def blog(request):
	posts = BlogContent.objects.all()
	return render(request,"blog.html",{"posts" : posts})

def blog_post(request,id = None):
	post = BlogContent.objects.get(pk=id)
	return render(request,"blog_post.html",{"post" : post})

def product_detail(request,id=None):
	product = ShopProduct.objects.get(pk=id)
	return render(request,"product_detail.html",{
			"product" : product,
			}
		)

def contact(request):
	if request.method == "POST":
		form_contact = forms.ContactForm(data=request.POST)
		if form_contact.is_valid():
			contact_info = form_contact.save()
			contact_info.save()
			messages.success(request,"<font color='#38a7bb'> We receive your information,we will reponse to you soon </font>",extra_tags="safe")
		else:
			print(form_contact.errors)
	else:
		form_contact = forms.ContactForm()
	return render(request,"contact.html",{'form_contact':form_contact})


def login(request):
	if request.method == "POST":
		form_login = forms.LoginForm(data=request.POST)
		if form_login.is_valid():
			username = form_login.cleaned_data['username']
			password = form_login.cleaned_data['password']
			authentication = authenticate(username=username,password=password)
			if authenticate is not None:
				return redirect('/')
			else:
				return render(request,"login.html",{'form_login':form_login})

	else:
		form_login = forms.LoginForm()

	return render(request,"login.html",{'form_login':form_login})


def register(request):
	if request.method == "POST":
		register_form = forms.RegisterForm(data=request.POST)
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			messages.success(request, 'Thanks for registering.You now can login with username <font color="#38a7bb"> %s </font>' % username,extra_tags='safe')
			user_profile = UserProfile(username=username)
			user_profile.save()

			register_info = register_form.save()
			register_info.save()
			#return render(request,"register.html",{'register_form':register_form})
		
	else:
		register_form = forms.RegisterForm()

	return render(request,"register.html",{'register_form':register_form})

def user_profile(request,username=None):
	user = User.objects.get(username=username)
	user_profile = UserProfile.objects.get(username=username)
	if request.method == "POST":
		user_form = forms.UserProfileForm(data=request.POST)
		if user_form.is_valid():
			data = user_form.cleaned_data
			user.first_name = data['first_name']
			user.last_name = data['last_name']
			user.save()

			user_profile.company = data['company']
			user_profile.country = data['country']
			user_profile.state = data['state']
			user_profile.address = data['address']
			user_profile.telephone = data['telephone']
			user_profile.save()

	else:
		user_form = forms.UserProfileForm()

	return render(request,"user_profile.html",{"user_form":user_form,"user_profile" : user_profile})

def shop(request,category=None):
	id = 0
	if category == "Books":
		id += 1
	elif category == "Laptops":
		id += 2
	elif category == "Smartwatch":
		id += 3
	elif category == "NetworkDevices":
		id += 4

	if id == 0:
		products = ShopProduct.objects.all()
	else:
		products = ShopProduct.objects.filter(category=id).order_by('name')

	return render(request,"shop.html",{
		"products" : products,
		}
	)

@require_POST
def cart_add(request, item_id = None):
	cart = Cart(request)
	product = ShopProduct.objects.get(id=item_id)
	form = forms.CartForm(data=request.POST)
	if form.is_valid():
		cart.add(product, product.price, form.cleaned_data['quantity'])
	return redirect('cart_detail')

def cart_remove(request, item_id = None):
	product = ShopProduct.objects.get(id=item_id)
	cart = Cart(request)
	cart.remove(product)
	return redirect('cart_detail')

@require_POST
def cart_update(request,item_id = None):
	cart = Cart(request)
	product = ShopProduct.objects.get(id = item_id)
	form = forms.CartForm(data=request.POST)
	if form.is_valid():
		data = form.cleaned_data
		cart.update(product,data['quantity'],data['unit_price'])
	return redirect('cart_detail')

def cart_detail(request):
	return render(request,"cart_detail.html",{'cart' : Cart(request)})

def checkout(request):
	cart = Cart(request)
	if request.method == "POST":
		form = forms.CheckOutForm(data=request.POST)
		if form.is_valid():
			user_email = form.cleaned_data['email']
			order = form.save()
			order.save()
			for item in cart:
				product = ShopProduct.objects.get(pk=item.product.pk)
				product.ordered_times += item.quantity
				product.save()
				OrderProduct.objects.create(purchase = order,product = item.product,price = item.unit_price)

			send_mail(user_email,cart)
			cart.clear()
			messages.success(request, '<font color="#38a7bb"> Thank you for purchasing our products </font>',extra_tags='safe')
	else:
		form = forms.CheckOutForm()

	return render(request,"checkout.html",{"checkout_form" : form})

def send_mail(user_email,cart):
	subject = "Success purchased courses"
	from_email = "michaelrossa0612@gmail.com"
	to_email = [user_email]
	ctx = {'cart' : cart}
	message = get_template("mail.html").render(ctx)

	email_obj = EmailMessage(subject,message,from_email,to_email)
	email_obj.content_subtype="html"
	email_obj.send()

def view_chart(request):
	products_list = ShopProduct.objects.order_by('name')
	name = []
	ordered_times = []
	for entry in products_list:
		name.append(entry.name)
		ordered_times.append(entry.ordered_times)

	times = {
		'name' : 'ordered times',
		'data' : ordered_times,
		'color' : '#38a7bb'
	}

	chart = {
		'chart' : {'type' : 'column'},
		'title' : {'text' : 'Ordered times'},
		'xAxis' : {'categories' : name},
		'series' : [times]
	}

	dump = json.dumps(chart)

	result = ""
	time_now = datetime.datetime.now()
	ordered_times1 = []
	label_list = ['id','name','ordered times']
	ordered_times1.append(label_list)

	for item in products_list:
		product = [item.id,item.name,item.ordered_times]
		ordered_times1.append(product)
	if request.method == "POST":
		file_name = "products" + time_now.strftime('%d-%m-%Y-%H-%M-%S') + ".xlsx"
		desktop = os.path.join(os.path.join(os.environ['HOME']),'Desktop')
		path = desktop + '/' + file_name
		write_excel(path,ordered_times1)
		result = "Saved file to" + path

	return render(request,"chart.html",{"chart" : dump,"result" : result})

def write_excel(path,write_list):
	workbook = xlsxwriter.Workbook(path)
	worksheet = workbook.add_worksheet()

	row = 0
	for item in write_list:
		i = 0
		while i < len(item):
			worksheet.write(row,i,item[i])
			i+=1
		row += 1
	workbook.close()
	return