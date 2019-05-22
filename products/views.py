from django.shortcuts import render, Http404

from .models import Productwithimage, photoframe, Producttype


def home(request):
    products = Productwithimage.objects.all()
    photoframes = photoframe.objects.all()
    producttypes = Producttype.objects.all()
   

    context = {'products': products, 'photoframes': photoframes, 'producttypes':producttypes}
    template = 'products/home.html'
    return render(request, template, context)


def about(request):
    producttypes = Producttype.objects.all()
    return render(request, 'products/about.html', {'title': 'About', 'producttypes':producttypes})

def returnpolicy(request):
    producttypes = Producttype.objects.all()
    return render(request, 'products/returnpolicy.html', {'title': 'Return Policy','producttypes':producttypes})
def tnc(request):
    producttypes = Producttype.objects.all()
    return render(request, 'products/termsandconditions.html', {'title': 'Terms and Conditions','producttypes':producttypes}) 

def all(request):
    producttypes = Producttype.objects.all()
    products = Productwithimage.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)



def single(request, slug):
    try:
        product = Productwithimage.objects.get(slug=slug)
        context = {'product': product}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404

    #try:
     #   product = Productwithimage.objects.get(slug=slug)
      #  context = {'products': products}
       # template = 'products/single.html'
        #return render(request, template, context)
    #except:
     #   raise Http404
def producttype(request, slug):
   # producttype = Producttype.objects.get(slug=slug)
    producttypes = Producttype.objects.all()
    products = Productwithimage.objects.all()
    context = { 'products': products,'producttypes':producttypes}
    template = 'products/category.html'
    return render(request, template, context)
 





def search(request):
    try:
        search = request.GET.get('search')
    except:
        search = None
    if search:
        products = Productwithimage.objects.filter(title__icontains=search)
        photoframes = photoframe.objects.filter(title__icontains=search)
        context = {'query': search, 'products': products, 'photoframes': photoframes}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
        context = {}
    return render(request, template, context)
