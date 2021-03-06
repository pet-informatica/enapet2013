from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from home.views import BaseView
from django.core.mail import mail_admins
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from django.core.mail import EmailMessage


class SubmitView(BaseView):
	def get_context_data(self, **kwargs):
		context = super(SubmitView, self).get_context_data(**kwargs)
		return context

	def post(self, request):
		dic = {}
		dic["name"] = request.POST.get("your-name") or ""
		dic["email"] = request.POST.get("email") or ""
		dic["subject"] = request.POST.get("subject") or ""
		dic["message"] = request.POST.get("message") or ""

		subject = "[CONTATO-ENAPET] %(name)s - %(subject)s" % dic
		emailFrom = 'phrd@cin.ufpe.br'
		message = """ 
		Nome: %(name)s
		Assunto: %(subject)s
		E-mail: %(email)s

		%(message)s
		"""% dic

		email = EmailMessage(subject, message, to=["enapet2013@gmail.com"])
		email.send()
		
		return HttpResponseRedirect('/contact/')


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

		send_mail(subject, message , 'enapet@contato.ufpe.br', ['dnr2@cin.ufpe.br'], fail_silently=False)		
		

def envia_email(name, to_email, html_path, password='', subject='Contato ENAPET 2013'):
    if not '@' in to_email:
            return
    if '@facebook.com' in to_email:
            return
    context = {
            'nome' : name,
            'email' : to_email,
            'senha' : password,
    }

    from_email = 'noreply@greaton.me'

    text_content = ''
    html_content = render_to_string(html_path, context)
    msg = 	(subject,
            text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
