from django import forms

from .models import Image, BetterThan


class ImageComparisonForm(forms.Form):

	a_better_than_b = forms.BooleanField(required=False)
	a = forms.ModelChoiceField(queryset=Image.objects.all(), widget=forms.HiddenInput())
	b = forms.ModelChoiceField(queryset=Image.objects.all(), widget=forms.HiddenInput())

	def __init__(self, *args, **kwargs):
		super(ImageComparisonForm, self).__init__(*args, **kwargs)

		import random

		a_random_idx = random.randint(0, Image.objects.count() - 1)
		random_obj = Image.objects.all()[a_random_idx]

		self.initial['a'] = random_obj
		self.a_image_url = random_obj.image.url

		b_random_idx = random.randint(0, Image.objects.count() - 1)

		while a_random_idx == b_random_idx:
			b_random_idx = random.randint(0, Image.objects.count() - 1)
		random_obj = Image.objects.all()[b_random_idx]

		self.initial['b'] = random_obj
		self.b_image_url = random_obj.image.url


	def save(self):
		if self.cleaned_data.get('a_better_than_b', False):
			to_return = BetterThan.objects.create(
				better_than=self.cleaned_data.get('a'),
				worse_than=self.cleaned_data.get('b'))
		else:
			to_return = BetterThan.objects.create(
				better_than=self.cleaned_data.get('b'),
				worse_than=self.cleaned_data.get('a'))
		return to_return