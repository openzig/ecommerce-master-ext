from django.shortcuts import render, Http404

# Create your views here.

from marketing.forms import EmailForm
from marketing.models import MarketingMessage, Slider


from .models import Product, ProductImage

from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
import json

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
	print(sliders)
	products = Product.objects.all()
	template = 'products/home.html'	
	context = {
		"products": products,
		"sliders": sliders,
		}
	return render(request, template, context)


def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'	
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

def get_json(request, page):
	products = Product.objects.all()
	data = {}
	result = []
	cnt = 0
	for product in products:
		result_item = {}
		for item in product.productimage_set.all():
			result_item['image'] = item.image.url;
			result_item['height'] = 200
			result_item['width'] = 200
			break
		if result_item.get('image') != None:
			result.append(result_item)
			cnt += 1
	data['result'] = result
	data['total'] = cnt
	return HttpResponse(json.dumps(data), content_type = "application/json")
	
	
