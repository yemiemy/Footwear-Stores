from django.contrib import admin
from .models import Product, ProductImage, Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'timestamp'
	search_fields = ['title', 'description']
	list_display = ['title', 'price', 'active', 'updated']
	list_editable = ['price', 'active']
	list_filter = ['price', 'active']
	readonly_fields = ['timestamp', 'updated']
	prepopulated_fields = {'slug': ('title',)}
	class Meta:
		model = Product

class ProductImageAdmin(admin.ModelAdmin):
	search_fields = ['slug', 'featured']
	list_display = ['slug','active', 'featured', 'adidas',
		'casual', 'female','male', 'givenchy', 'gucci', 'slip_ons', 'boots',
		'sandals', 'lace_ups', 'oxfords', 'nike'
	]

	list_editable = [
		'adidas', 'active', 'featured', 'givenchy', 'gucci', 'slip_ons', 'boots',
		'male', 'female', 'casual', 'sandals', 'lace_ups', 'oxfords', 'nike'
	]
	#prepopulated_fields = {'slug': ('product.title',)}
	class Meta:
		model = ProductImage

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Variation)