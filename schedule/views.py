from django.shortcuts import render

from models import Event
from home.views import BaseView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class HomeView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context["schedule"] = Event.objects.order_by('date_start').all()
		return context

	def get(self, request, page=1):
		return render(request, 'schedule.html', self.get_context_data())

class EventView(BaseView):
	def get_context_data(self, event_id=None, event_slug=None, **kwargs):
		context = super(EventView, self).get_context_data(**kwargs)
		if event_id:
			context['event'] = Event.objects.get(id=event_id)
		else:
			context['event'] = Event.objects.get(slug=event_slug)

		return context

	def get(self, request, event_id=None, event_slug=None):
		return render(request, 'event.html', self.get_context_data(event_id=event_id, event_slug=event_slug))
