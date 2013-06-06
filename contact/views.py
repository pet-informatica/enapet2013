from django.shortcuts import render

from home.views import BaseView
from django.core.mail import mail_admins

class HomeView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		return context

	def get(self, request):
		return render(request, 'contact.html', self.get_context_data())

	def post(self, request):
		dic = {}
		dic["name"] = request.POST.get("your-name") or ""
		dic["phone"] = request.POST.get("phone") or ""
		dic["subject"] = request.POST.get("subject") or ""
		dic["message"] = request.POST.get("message") or ""

		subject = "[CONTATO-ENAPET] %(name)s - %(subject)s" % dic
		message = """
		Nome: %(name)s
		Assunto: %(subject)s
		Telefone: %(phone)s

		%(message)s
		"""% dic

		mail_admins(subject, message)
