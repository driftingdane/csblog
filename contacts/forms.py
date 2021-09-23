from django import forms
from django.core.validators import validate_email


class ContactForm(forms.Form):
	name = forms.CharField(label="Navn", max_length="30", min_length="3", required=True, widget=forms.TextInput(attrs={'placeholder': 'Dit navn (minimum 3)'}))
	email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'placeholder': 'Din email'}))
	message = forms.CharField(label="Besked", required=True, widget=forms.Textarea(attrs={'placeholder': 'Din besked', 'cols': '5', 'rows': '5'}))

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control mb-3'
