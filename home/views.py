from django.shortcuts import render

from blog.models import Article
from schedule.models import Event

from django.views.generic.base import View

class BaseView(View):
	def get_context_data(self, **kwargs):
		context = {}
		context['footer_articles'] = Article.objects.filter(published=True).order_by('-date_published')[:5]
		return context

	def get_values(self):
		ret = dict((key, value) for key, value in self.__dict__.iteritems() if not callable(value) and not key.startswith('__'))
		return ret
		

class IndexView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['index_articles'] = Article.objects.filter(published=True).order_by('-date_published')[:3]
		context["schedule"] = Event.objects.order_by('date_start').all()
		return context

	def get(self, request):
		return render(request, 'index.html', self.get_context_data())

