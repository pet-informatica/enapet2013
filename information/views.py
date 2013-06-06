from django.shortcuts import render

from home.views import BaseView
from django.core.mail import mail_admins

class HomeView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		return context

	def get(self, request):
		return render(request, 'info.html', self.get_context_data())
