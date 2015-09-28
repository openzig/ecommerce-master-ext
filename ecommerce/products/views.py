from django.shortcuts import render, Http404

# Create your views here.

# from marketing.forms import EmailForm
from marketing.models import Slider


from .models import Product, ProductImage, Category

from django.http import HttpResponse
from django.conf import settings
import json
import random

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products': products}
		template = 'products/results.html'	
	else:
		template = 'products/home.html'	
		context = {}
	return render(request, template, context)


def home(request):
	sliders = Slider.objects.all()
	categories = Category.objects.all()
	template = 'products/home.html'	
	context = {
		"sliders": sliders,
		"categories" : categories,
		"category_title" : "LATEST PRODUCTS"
		}
	return render(request, template, context)


def category(request, slug):
	categories = Category.objects.all()
	category = Category.objects.get(slug=slug)
	# products = Product.objects.filter(category=category)
	context = {"categories" : categories, "category_title":category.title}
	template = 'products/category.html'	
	return render(request, template, context)


def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		#images = product.productimage_set.all()
		images = ProductImage.objects.filter(product=product)
		context = {'product': product, "images": images}
		template = 'products/single.html'	
		return render(request, template, context)
	except:
		raise Http404

def products_json(request, page):
	products = Product.objects.all()
	data = {}
	result = []
	cnt = 0
	for product in products:
		result_item = {}
		result_item['title'] = product.title
		result_item['url'] = product.get_absolute_url()
		result_item['price'] = str(product.price)
		result_item['sales'] = str(product.sales)
		for item in product.productimage_set.all():
			if item.featured:
				result_item['image'] = item.image.url;
				scaled_height = 1.0 * item.image.height * settings.WATERFALL_IMAGE_FIXED_WIDTH / item.image.width
				result_item['height'] = scaled_height
				result_item['width'] = settings.WATERFALL_IMAGE_FIXED_WIDTH
		if result_item.get('image') != None:
			result.append(result_item)
			cnt += 1
	data['result'] = result
	data['total'] = cnt
	return HttpResponse(json.dumps(data), content_type = "application/json")

def category_products_json(request, slug, page):
	category = Category.objects.get(slug=slug)
	print(category)
	products = Product.objects.filter(category=category)
	data = {}
	result = []
	cnt = 0
	for product in products:
		result_item = {}
		result_item['title'] = product.title
		result_item['url'] = product.get_absolute_url()
		result_item['price'] = str(product.price)
		result_item['sales'] = str(product.sales)
		for item in product.productimage_set.all():
			if item.featured:
				result_item['image'] = item.image.url;
				scaled_height = 1.0 * item.image.height * settings.WATERFALL_IMAGE_FIXED_WIDTH / item.image.width
				result_item['height'] = scaled_height
				result_item['width'] = settings.WATERFALL_IMAGE_FIXED_WIDTH
		if result_item.get('image') != None:
			result.append(result_item)
			cnt += 1
	data['result'] = result
	data['total'] = cnt
	return HttpResponse(json.dumps(data), content_type = "application/json")
	
	
