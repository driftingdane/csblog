from django.conf import settings

def key(request):
	site_key = settings.RECAPTCHA_SITE_KEY
	return {'site_key': site_key}