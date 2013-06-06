from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

class Message(models.Model):
	name = models.CharField(max_length=128)
	headline = models.CharField(max_length=140)
	place = models.CharField(max_length=140)
	content = HTMLField()
	
	date_start = models.DateTimeField()
	date_end = models.DateTimeField()
	tags = TaggableManager(blank=True)
	slug = models.SlugField()

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		else:
			self.slug = slugify(self.slug)

		super(Event, self).save(*args, **kwargs)
