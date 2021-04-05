from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact


def contact(request):
	if request.method == 'POST':
		
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		
		contact = Contact(name=name, email=email, message=message)
		
		contact.save()
		
		# Send mail
		send_mail(
			'Hello Admin. You have new mail',
			message,
			email,
			['tbhedelund@gmail.com'],
			fail_silently=False
		)
		
		messages.success(request, 'Your message was sent.')
		return redirect('blog:index')

