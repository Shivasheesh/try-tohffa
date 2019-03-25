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


class Productwithimage(models.Model):
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



class photoframe(models.Model):
	title = models.CharField(max_length=120, null= False, blank=False)
	description = models.TextField()
	price= models.DecimalField(decimal_places=2, max_digits=100, default=299.99)
	slug = models.SlugField()
	image = models.ImageField(upload_to='products/img/')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	shipdate = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)


		