from django.conf import settings
from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm


def contact(request):
	
	global name, email, message
	if request.method == 'POST':

		form = ContactForm(request.POST)
		secret_key = settings.RECAPTCHA_SECRET_KEY
		data = request.POST
		# captcha verification
		data = {
			'response': data.get('g-recaptcha-response'),
			'secret': secret_key
		}
		resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		result_json = resp.json()

		print(result_json)

		if not result_json.get('success'):
			messages.error(request, 'Duplicate mail or you are a robot')
			return redirect('blog:index')
		# end captcha verification

		# Validate the form: the captcha field will automatically
		# check the input
		if form.is_valid():
			name = request.POST['name']
			email = request.POST['email']
			message = request.POST['message']
		save_contact = Contact(name=name, email=email, message=message)

		save_contact.save()

		# Send mail
		send_mail(
			'Hello Admin. You have new mail',
			message,
			email,
			['driftingdane@gmail.com'],
			fail_silently=False
		)

		messages.success(request, 'Your message was sent.')
		return redirect('blog:index')
	else:
		form = ContactForm()
	return render(request, 'base.html', {'form': form})
