from phantomapp.models import *
from django.contrib import admin

admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(BlogLabel)
admin.site.register(BlogContent)
admin.site.register(ShopCategory)
admin.site.register(ShopProduct)

class OrderProductInLine(admin.TabularInline):
	model = OrderProduct
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','username','email','first_name','last_name','country','state','address','telephone']
	list_filter = ['paid','created','updated']
	inlines = [OrderProductInLine]

admin.site.register(Order,OrderAdmin)