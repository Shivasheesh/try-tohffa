from django.db import models
from django.conf import settings
from products.models import Productwithimage, Variation
# Create your models here.
class CartItem(models.Model):
	cart = models.ForeignKey('Cart', on_delete=models.PROTECT)
	product =models.ForeignKey(Productwithimage, on_delete=models.PROTECT)
	variations = models.ManyToManyField(Variation, blank=True)
	quantity =models.IntegerField(default=1)
	line_total = models.DecimalField(default=999.99, max_digits=1000, decimal_places=2)
	notes = models.TextField(null=True, blank=True)
	timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)
	updated =models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title



class Cart(models.Model):
	total =models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp =models.DateTimeField(auto_now_add=True, auto_now=False)
	updated =models.DateTimeField(auto_now_add=False, auto_now=True)
	active =models.BooleanField(default=True)

	def __unicode__(self):
		return "Cart id: %s" %(self.id)
