from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control mb-3'