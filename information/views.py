from django.shortcuts import render

from home.views import BaseView
from django.core.mail import mail_admins

class HomeView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		return context

	def get(self, request):
		return render(request, 'info.html', self.get_context_data())

class EventView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(EventView, self).get_context_data(**kwargs)
		return context

	def get(self, request):
		return render(request, 'info-event.html', self.get_context_data())

class CityView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(CityView, self).get_context_data(**kwargs)
		return context

	def get(self, request):
		return render(request, 'info-city.html', self.get_context_data())

class InfrastructureView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(InfrastructureView, self).get_context_data(**kwargs)
		return context

	def get(self, request):
		return render(request, 'info-infrastructure.html', self.get_context_data())

class MeetingView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(MeetingView, self).get_context_data(**kwargs)
		return context

	def get(self, request):
		return render(request, 'info-meeting.html', self.get_context_data())
