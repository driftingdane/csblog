from .forms import ContactForm
from django.utils.translation import gettext_lazy as _


def contactform(request):
	return {'form': ContactForm()}
