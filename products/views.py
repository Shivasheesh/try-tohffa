from django.shortcuts import render

from .models import Productwithimage, photoframe



def home(request):
	products = Productwithimage.objects.all()
	photoframes = photoframe.objects.all()
	context = {'products': products, 'photoframes': photoframes}
	template = 'products/home.html'
	return render(request, template, context )

def about(request):
	return render(request, 'products/about.html', { 'title': 'About' })

def all(request):
	products = Productwithimage.objects.all()
	context={'products': products}
	template = 'products/all.html'
	return render(request, template, context)



def single(request,slug):
	try:
		product = Productwithimage.objects.get(slug=slug)
		context={'product': product}  
		template = 'products/single.html'
		return render(request, template, context)
	except:
		raise Http404

def search(request):
	try:
		search = request.GET.get('search')
	except:
		search = None
	if search:
		products = Productwithimage.objects.filter(title__icontains=search)
		photoframes = photoframe.objects.filter(title__icontains=search)
		context = {'query':search, 'products': products, 'photoframes': photoframes}
		template = 'products/results.html'
	else:
		template = 'products/home.html'
		context = {}
	return render(request, template, context)

