from phantomapp import views
from django.urls import path
from django.contrib import auth
from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^about/$',views.about,name="about"),
	url(r'^blog/$',views.blog,name="blog"),
	url(r'^blog/post/(\d+)/$',views.blog_post,name="blog_post"),
	url(r'^contact/$',views.contact,name="contact"),
	url(r'^login/$',LoginView.as_view(template_name="login.html"),name="login"),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^register/$',views.register,name="register"),
	url(r'^portfolio/$',views.portfolio,name="portfolio"),
	url(r'^users/profile/(?P<username>[a-zA-Z0-9]+)$',views.user_profile,name="user_profile"),
	url(r'^shop/category/(?P<category>[a-zA-Z0-9]+)$',views.shop,name="shop"),
	url(r'^shop/product/(\d+)',views.product_detail,name="product_detail"),
	url(r'^shop/checkout/$',views.checkout,name="checkout"),
	url(r'^cart_add/(\d+)/$',views.cart_add,name="cart_add"),
	url(r'^cart/remove/(\d+)/$',views.cart_remove,name="cart_remove"),
	url(r'^cart/detail/$',views.cart_detail,name="cart_detail"),
	url(r'^cart/update/(\d+)/$',views.cart_update,name="cart_update"),
	url(r'^rss/$',views.rss,name="rss"),
	url(r'^chart/$',views.view_chart,name="chart"),
]