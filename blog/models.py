from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField

class Article(models.Model):
	title = models.CharField(max_length=128)
	headline = models.CharField(max_length=140)
	content = HTMLField()
	teaser = models.TextField()
	date_published = models.DateTimeField(auto_now_add=True)
	published = models.BooleanField()
	author = models.ForeignKey(User)
	tags = TaggableManager(blank=True)
	slug = models.SlugField()

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		else:
			self.slug = slugify(self.slug)

		super(Article, self).save(*args, **kwargs)
