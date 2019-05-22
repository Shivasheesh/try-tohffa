from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from products.models import Productwithimage, Variation

from .models import Cart, CartItem

def view(request):
	try:
		the_id =request.session['cart_id']
	except:
		the_id =None
	if the_id:
		cart = Cart.objects.get(id=the_id)
		new_total = 0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			new_total += line_total

		request.session['items_total']= cart.cartitem_set.count()
		cart.total = new_total
		cart.save()
		context ={"cart":cart}
	else :
		empty_message ="Your cart is currently empty!"
		context ={"empty": True, "empty_message": empty_message}
		
	template ="carts/view.html"  
	return render(request, template, context)

def remove_from_cart(request, id):
	try:
		the_id =request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse("cart"))

	cartitem = CartItem.objects.get(id=id)
	cartitem.delete()
	#cartitem.cart = None
	#cartitem.save()

	return HttpResponseRedirect(reverse("cart"))
		


def add_to_cart(request, slug):
	request.session.set_expiry(30000)



	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id =new_cart.id

	cart = Cart.objects.get(id=the_id)

	try:
		product = Productwithimage.objects.get(slug=slug)
	except Productwithimage.DoesNotExist:
		pass
	except:
		pass

	product_var = [] #product_variation
	if request.method == "POST":
		qty = request.POST['qty']

		for item in request.POST:
			key = item
			val = request.POST[key] 
			try: 
				v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
				product_var.append(v)
			except: 
				pass
		cart_item = CartItem.objects.create(cart=cart, product=product)
		if len(product_var) > 0:
			cart_item.variations.add(*product_var)
		cart_item.quantity = qty
		cart_item.save()
		#success message (possible)

	
	

		
		return HttpResponseRedirect(reverse("cart"))

	return HttpResponseRedirect(reverse("cart"))




	


