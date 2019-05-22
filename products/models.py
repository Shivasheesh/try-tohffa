from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User





class Product(models.Model):
	title = models.CharField(max_length=120, null= False, blank=False)
	description = models.TextField()
	price= models.DecimalField(decimal_places=2, max_digits=100, default=299.99)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	shipdate = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

	def __unicode__(self):
		return self.title


class Producttype(models.Model):
	title = models.CharField(max_length=120, null= False, blank=False)
	description = models.TextField()
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.title
	class Meta:
		unique_together =('title', 'slug')

	def get_absolute_url(self):
		return reverse("product-type", kwargs={"slug": self.slug})

class Productwithimage(models.Model):
	title = models.CharField(max_length=120, null= False, blank=False)
	description = models.TextField()
	category = models.ForeignKey(Producttype, on_delete=models.PROTECT)
	price= models.DecimalField(decimal_places=2, max_digits=100, default=299.99)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='products/img/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	shipdate = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

	def __unicode__(self):
		return self.title
	class Meta:
		unique_together =('title', 'slug')

	def get_absolute_url(self):
		return reverse("single-product", kwargs={"slug": self.slug})


class VariationManager(models.Manager):
	def all(self):
		return super(VariationManager, self).filter(active=True)

	def sizes(self):
		return super(VariationManager, self).filter(active=True).filter(category='size')

	def colors(self):
		return super(VariationManager, self).filter(active=True).filter(category='color')


VAR_CATEGORIES = (
	('size', 'size'),
	('color', 'color'),
	('package', 'package'),
	)


class photoframe(models.Model):
	title = models.CharField(max_length=120, null= False, blank=False)
	description = models.TextField()
	price= models.DecimalField(decimal_places=2, max_digits=100, default=299.99)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='products/img/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	shipdate = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

	def __unicode__(self):
		return self.title
	class Meta:
		unique_together =('title', 'slug')

class Variation(models.Model):
	product = models.ForeignKey(Productwithimage,  on_delete=models.PROTECT)
	category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
	title = models.CharField(max_length=120)
	price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	objects= VariationManager()

	def __unicode__(self):
		return self.title


		