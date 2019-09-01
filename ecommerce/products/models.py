from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return '{}'.format(self.title)

	class Meta:
		unique_together = ('title', 'slug')
		


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	slug = models.SlugField(default=True)
	image = models.ImageField(upload_to='products/images/')
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	featured = models.BooleanField(default=False)
	male = models.BooleanField(default=False)
	female = models.BooleanField(default=False)
	casual = models.BooleanField(default=False)
	sport = models.BooleanField(default=False)
	formal = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	nike = models.BooleanField(default=False)
	adidas = models.BooleanField(default=False)
	givenchy = models.BooleanField(default=False)
	gucci = models.BooleanField(default=False)
	slip_ons = models.BooleanField(default=False)
	boots = models.BooleanField(default=False)
	sandals = models.BooleanField(default=False)
	lace_ups = models.BooleanField(default=False)
	oxfords = models.BooleanField(default=False)
	black = models.BooleanField(default=False)
	white = models.BooleanField(default=False)
	blue = models.BooleanField(default=False)
	red = models.BooleanField(default=False)
	green = models.BooleanField(default=False)
	grey = models.BooleanField(default=False)
	orange = models.BooleanField(default=False)
	brown = models.BooleanField(default=False)
	leather = models.BooleanField(default=False)
	suede = models.BooleanField(default=False)

	def __str__(self):
		return "{}'s image ".format(self.product.title)


class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return self.all().filter(category='size')
	def colors(self):
		return self.all().filter(category='color')



VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	('package', 'package'),
	)

class Variation(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	title = models.CharField(max_length=120)
	image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.CASCADE)
	price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=100)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	objects = VariationManager()

	def __str__(self):
		return self.title