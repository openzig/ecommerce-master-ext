from django.core.urlresolvers import reverse
from django.db import models
# from django.db.models.signals import post_save
# Create your models here.
from django import template

register = template.Library()

class Category(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True)
	featured = models.BooleanField(default=None)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)


	def __str__(self):
		return self.title

# T-Shirt 1
# Active Wear 2
# Women's Clothing 3


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	category = models.ManyToManyField(Category, null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=65, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=65,\
												null=True, blank=True)
	sales = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='products/images/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.title

class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def get_variations(self):
		category_set = self.all().values('category').distinct();
		variations = []
		for category_item in category_set:
			variation = {}
			variation['category'] = category_item['category']
			variation['title'] = []
			variation['price'] = []
			values = self.all().filter(category=category_item['category'])
			for value in values:
				variation['title'].append(value.title)
				variation['price'].append(value.price)
			variations.append(variation)
		return variations

class Variation(models.Model):
	product = models.ForeignKey(Product)
	category = models.CharField(max_length=120)
	title = models.CharField(max_length=120)
	# image = models.ForeignKey(ProductImage, null=True, blank=True)
	price = models.DecimalField(max_digits=65, decimal_places=2, null=True, blank=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	
	objects = VariationManager()

	def __str__(self):
		return self.title
	